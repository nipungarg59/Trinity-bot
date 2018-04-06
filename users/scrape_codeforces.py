import copy
import json
import requests

from django.db.models import Q

from users import constants as constants
from users.models import Contests, Dictionary


def make_hash(o):
    """
    Makes a hash from a dictionary, list, tuple or set to any level, that contains
    only other hashable types (including any lists, tuples, sets, and
    dictionaries).
    """
    if isinstance(o, (set, tuple, list)):
        return tuple([make_hash(e) for e in o])

    elif not isinstance(o, dict):
        return hash(o)

    new_o = copy.deepcopy(o)
    keys = list(new_o.keys())
    for key in keys:
        if 'Seconds' in key:
            del new_o[key]

    for k, v in new_o.items():
        new_o[k] = make_hash(v)

    return hash(tuple(frozenset(sorted(new_o.items()))))


def scrape_contest_list_helper(start=1, gym=False):
    """
    This will scrape all the codeforces contest list
    :return:
    """
    if gym:
        url = constants.CODEFORCES_GYM_CONTEST_LIST_URL
    else:
        url = constants.CODEFORCES_REGULAR_CONTEST_LIST_URL

    contest_list = requests.get(url)
    _hash = make_hash(json.loads(contest_list.content.decode('utf-8')))

    cache_list, created = Dictionary.objects.get_or_create(key='hash', defaults={'value': _hash})

    contest_list_data = []

    if created or cache_list.value != _hash:
        cache_list.value = _hash
        cache_list.save()

        for contest in json.loads(contest_list.content.decode('utf-8'))['result']:
            if contest['id'] >= start:
                contest_list_data.append(contest)

    return sorted(contest_list_data, key=lambda k: k['id'])


def scrape_contest_list(gym=False):
    last_contest = Contests.objects.filter(~Q(phase='FINISHED'), platform='Codeforces').order_by("id").first()
    start = 1
    # if last_contest:
    #     start = last_contest.platform_id
    #
    # contest_list = scrape_contest_list_helper(start=start, gym=gym)
    #
    # for contest in contest_list:
    #     contest_db, created = Contests.objects.get_or_create(platform='Codeforces', platform_id=contest['id'])
    #     contest_db.type = contest['type']
    #     contest_db.phase = contest['phase']
    #     contest_db.frozen = contest['frozen']
    #     contest_db.duration_seconds = contest['durationSeconds']
    #     contest_db.start_time = contest['startTimeSeconds']
    #     contest_db.save()
    from users.tasks import send_message
    send_message.delay('453502085', 'Scraped')
