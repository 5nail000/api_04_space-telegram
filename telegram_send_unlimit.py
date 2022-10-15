import time
import random

from base_functions import *
from telegram_send_photo import *


def send_telegram_unlimit(token, chat_id, sleep_time = 4, folder = 'images'):
    
    all_images = pick_all_imagefiles(folder)
    while True:
        for image in all_images:
            send_telegram_photo(token= token, chat_id= chat_id, image= image)
            time.sleep(60*60*float(sleep_time))
        random.shuffle(all_images)


if __name__ == '__main__':

    send_telegram_unlimit(token= BOT_TOKEN, chat_id= CHAT_ID, sleep_time= SLEEP_HOURS)