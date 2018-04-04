from __future__ import absolute_import

import os

from django.conf import settings

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Trinity.settings')
app = Celery('Trinity')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'users.tasks.send_message',
        'schedule': 5.0,
        'args': (453502085, "Hello 5")
    },
}