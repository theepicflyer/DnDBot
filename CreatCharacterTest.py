from telegram import Updater

updater = Updater(token="152501487:AAElGigfjuICcLgXT4U2qu74OQyxmjQQ8Ho")
dispatcher = updater.dispatcher


class Character(object):
    def __init__(self, name):
        self.name = name

def start(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = "This is kaitlynbot.")

def createCharacter(bot, update):
    update.message.first_name = Character(update.message.text)
    bot.sendMessage(chat_id = update.message.chat_id, text = "The character %s has been created!" % (____.name))

def unknown(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = "Sorry, I didn't understand that!")

    

dispatcher.addTelegramCommandHandler('start', start)
dispatcher.addTelegramCommandHandler('createperson', createPerson)
dispatcher.addUnknownTelegramCommandHandler(unknown)                

updater.start_polling()
    
