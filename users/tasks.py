import os
import requests

from Trinity.celery import app
from users.scrape_codeforces import scrape_contest_list

@app.task
def send_message(chat_id, message, mode='Markdown'):
    url = os.environ['telegram_base_api'] + 'sendMessage'
    payload = {
        'chat_id': chat_id,
        'parse_mode': mode,
        'text': message
    }
    requests.post(url, data=payload)


@app.task
def scrape_codeforces_contest():
    scrape_contest_list()
