from telegram import Updater

updater = Updater(token="152501487:AAElGigfjuICcLgXT4U2qu74OQyxmjQQ8Ho")
dispatcher = updater.dispatcher

def user(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = update.message.from_user.first_name)

dispatcher.addTelegramCommandHandler('user', user)
updater.start_polling()
