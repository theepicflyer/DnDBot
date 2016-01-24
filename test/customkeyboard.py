from telegram import *

updater = Updater(token="152501487:AAElGigfjuICcLgXT4U2qu74OQyxmjQQ8Ho")
dispatcher = updater.dispatcher

def custom(bot, update):
    keyboard = [
            ['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            ['0']
        ]

    reply_markup = ReplyKeyboardMarkup.create(keyboard)
    bot.send_message(chat_id = update.message.chat_id, text = 'please enter a number', reply_markup=reply_markup)

dispatcher.addTelegramCommandHandler('custom', custom)

updater.start_polling()

