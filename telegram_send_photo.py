import argparse
import os
import random
import time

import telegram
from telegram.ext import Updater
from dotenv import load_dotenv
from os.path import isfile

from base_functions import pick_all_imagefiles


def send_telegram_photo(token, chat_id, image, caption=None):

    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    with open(image, 'rb') as image_file:
        try:
            dp.bot.send_photo(chat_id=chat_id, photo=image_file, caption=caption)
        except telegram.error.NetworkError:
            time.sleep(5)
            return False


if __name__ == '__main__':

    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    tg_chat_id = os.environ['TG_CHAT_ID']

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', help="image filename", type=str, default=random.choice(pick_all_imagefiles()))
    args = parser.parse_args()

    if isfile(args.image):
        send_telegram_photo(token=tg_token, chat_id=tg_chat_id, image=args.image)
    else:
        print('You entered the wrong filename, the file does not exist.')
