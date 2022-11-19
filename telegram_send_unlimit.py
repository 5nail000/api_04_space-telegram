import os
import time
import random

from base_functions import pick_all_imagefiles
from telegram_send_photo import send_telegram_photo
from dotenv import load_dotenv


def send_telegram_unlimit(token, chat_id, sleep_time=4, folder='images'):

    all_images = pick_all_imagefiles(folder)
    while True:
        for image in all_images:
            send_telegram_photo(token=token, chat_id=chat_id, image=image)
            time.sleep(60*60*sleep_time)
        random.shuffle(all_images)


if __name__ == '__main__':

    load_dotenv()

    sleep_hours = float(os.getenv('SLEEP_HOURS', default=4))
    tg_token = os.environ['TG_TOKEN']
    tg_chat_id = os.environ['TG_CHAT_ID']
    send_telegram_unlimit(token=tg_token, chat_id=tg_chat_id, sleep_time=sleep_hours)
