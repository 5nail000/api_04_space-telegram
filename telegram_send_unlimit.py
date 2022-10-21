import os
import time
import random

from base_functions import pick_all_imagefiles
from telegram_send_photo import send_telegram_photo
from dotenv import load_dotenv


def send_telegram_unlimit(token, chat_id, sleep_time = 4, folder = 'images'):
    
    all_images = pick_all_imagefiles(folder)
    while True:
        for image in all_images:
                send_telegram_photo(token= token, chat_id= chat_id, image= image)
                time.sleep(60*60*float(sleep_time))
        random.shuffle(all_images)


if __name__ == '__main__':

    load_dotenv()
    TG_TOKEN = os.getenv('TG_TOKEN')
    TG_CHAT_ID = os.getenv('TG_CHAT_ID')
    SLEEP_HOURS = os.getenv('SLEEP_HOURS')

    send_telegram_unlimit(token= TG_TOKEN, chat_id= TG_CHAT_ID, sleep_time= SLEEP_HOURS)