from telegram import Updater

updater = Updater(token="152501487:AAElGigfjuICcLgXT4U2qu74OQyxmjQQ8Ho")
dispatcher = updater.dispatcher

characterlist = []
playerIndex = 0

class Character(object):
    playername = None
    charactername = None
    race = None
    _class = None
    stats = {}
    def __init__(self, charactername, playername):
        self.playername = playername
        self.charactername = charactername

def start(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = "Welcome to Dungeons and Dragons.")

def createCharacter(bot, update):
    playerIndex += 1
    playername = update.message.from_user.first_name
    charactername = update.message.text[17:]
    print (charactername)
    characterlist.append(Character(playername, charactername))  
    #bot.sendMessage(chat_id = update.message.chat_id, text = "The character %s has been created!" % (charactername))

def findCharacterIndex(first_name):
    for i in characterlist:
        if characterlist[i].playername == first_name:
            return i

def unknown(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = "Sorry, I didn't understand that!")

dispatcher.addTelegramCommandHandler('start', start)
dispatcher.addTelegramCommandHandler('createcharacter', createCharacter)
dispatcher.addUnknownTelegramCommandHandler(unknown)                

updater.start_polling()
