import os
import random
from telegram.ext import Updater
from urllib.parse import urlparse
from dotenv import load_dotenv

from base_functions import pick_all_imagefiles


def send_telegram_photo(token, chat_id, image = None, caption = None):
    
    updater = Updater(token, use_context = True)
    dp = updater.dispatcher
    
    if image is None:
        image = random.choice(pick_all_imagefiles())

    parsed_link = urlparse(image)
    if parsed_link.hostname is None: 
        with open(image, 'rb') as image_file:
            try:
                dp.bot.send_photo(chat_id= chat_id, photo= image_file, caption= caption)
            except:
                return False
    else: 
        try:
            dp.bot.send_photo(chat_id= chat_id, photo=image, caption= caption)
        except:
            return False
        

if __name__ == '__main__':

    load_dotenv()
    try:
        tg_token = os.environ['TG_TOKEN']
        tg_chat_id = os.environ['TG_CHAT_ID']
    except Exception as _ex: 
        print (f'KeyError: {_ex}')
    else:
        send_telegram_photo(token= tg_token, chat_id= tg_chat_id)