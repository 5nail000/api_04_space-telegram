from telegram.ext import *
import telegram

#from telegram.ext import Updater
#from telegram.ext import  ContextTypes, CommandHandler
#from telegram.ext import filters, MessageHandler, CommandHandler, ContextTypes

BOT_TOKEN = '5778281282:AAHAPOtzeP7_qofFxkkb0KxgSJzhMarWn-Y'
CHAT_ID = -1001839847575


def start_command(update, context):
    name = update.message.chat.first_name
    update.message.reply_text("Hello " + name)


def image_downloader(update, context):
    print (update.message['caption'])

    file = update.message.photo[-1].file_id
    obj = context.bot.get_file(file)
    obj.download()   

    update.message.reply_text("Image received")


def main():

    print("Started")
    TOKEN = BOT_TOKEN

    updater = Updater(TOKEN, use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(MessageHandler(Filters.photo, image_downloader))

    #dp.bot.send_message(chat_id= -1001839847575, text='YO!!!!!')
    dp.bot.send_photo(chat_id= -1001839847575, photo=open('images/file_0.jpg', 'rb'))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()