import random
from telegram.ext import *
from urllib.parse import urlparse

from base_functions import *


def send_telegram_photo(token, chat_id, image = None, caption = None):
    
    updater = Updater(token, use_context = True)
    dp = updater.dispatcher
    
    if image is None:
        image = random.choice(pick_all_imagefiles())

    parsed_link = urlparse(image)
    if parsed_link.hostname is None: 
        dp.bot.send_photo(chat_id= chat_id, photo=open(image, 'rb'), caption= caption)
    else: dp.bot.send_photo(chat_id= chat_id, photo=image, caption= caption)

if __name__ == '__main__':

    load_dotenv()
    TG_TOKEN = os.getenv('TG_TOKEN')
    TG_CHAT_ID = os.getenv('TG_CHAT_ID')

    send_telegram_photo(token= TG_TOKEN, chat_id= TG_CHAT_ID)