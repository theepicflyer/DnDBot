from telegram import *

updater = Updater(token="INSERT YOUR TOKEN HERE")
dispatcher = updater.dispatcher

def Custom(bot, update):
    custom_keyboard = [[ telegram.Emoji.THUMBS_UP_SIGN, telegram.Emoji.THUMBS_DOWN_SIGN ]]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.sendMessage(chat_id=chat_id, text="Stay here, I'll be back.", reply_markup=reply_markup)

def start(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = "Custom keyboard!")

dispatcher.addTelegramCommandHandler('start', start)
dispatcher.addTelegramCommandHandler('custom', Custom)

updater.start_polling()
