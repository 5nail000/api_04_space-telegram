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
    #send_telegram_photo(token= BOT_TOKEN, chat_id= CHAT_ID, image= 'images/file_0.jpg')
    #send_telegram_photo(token= BOT_TOKEN, chat_id= CHAT_ID, image= 'https://img-10.wfolio.com/NBYVWm12vATkBOfbWKesnOMTEiOFEP8qrU0v2Ig6UGc/rs:fit:1280:0:0/cb:v1/aHR0cDovL3N0b3Jh/Z2Uud2ZvbGlvLnJ1/L3NpdGVzLzMwMTQ5/L2Fzc2V0cy8xNjQ4/NTc2MTI4XzI0NmFl/ZC5qcGc', caption= 'view')

    send_telegram_photo(token= BOT_TOKEN, chat_id= CHAT_ID)