import os

import requests

RECAPTCHA_SECRET_KEY = os.getenv('CAPTCHA_SECRET_KEY')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

GOOGLE_RECAPTCHA_VERIFY_URL = 'https://www.google.com/recaptcha/api/siteverify'

URL = (f'https://api.telegram.org/'
       f'bot{TELEGRAM_TOKEN}/'
       f'sendMessage?'
       f'chat_id={TELEGRAM_CHAT_ID}'
       f'&text=')


def check_recaptcha(token):
    data = {
        'secret': RECAPTCHA_SECRET_KEY,
        'response': token
    }
    response = requests.post(GOOGLE_RECAPTCHA_VERIFY_URL, data=data)
    response = response.json()
    success = response.get('success')
    if success:
        return success
    return success


def send_telegram_message(message):
    result_url = URL + message
    requests.get(url=result_url)
