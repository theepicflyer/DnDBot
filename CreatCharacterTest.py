from telegram import Updater

updater = Updater(token="152501487:AAElGigfjuICcLgXT4U2qu74OQyxmjQQ8Ho")
dispatcher = updater.dispatcher

characterlist = []

class Character(object):
    playerCount = 0
    playername = None
    charactername = None
    race = None
    _class = None
    stats = {}
    def __init__(self, charactername, playername):
        playerCount += 1
        self.playername = playername
        self.charactername = charactername

def start(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = "Welcome to Dungeons and Dragons.")

def createCharacter(bot, update):
    charactername = update.message.text
    playername = update.message.from_user.first_name
    characterlist[Character.playerCount] = Character(charactername, playername)   
    bot.sendMessage(chat_id = update.message.chat_id, text = "The character %s has been created!" % (charactername))

def findCharacterIndex(bot, update):
    for i in characterlist:
        if characterlist[i].playername == update.message.from_user.first_name:
            return characterlist[i]

def unknown(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = "Sorry, I didn't understand that!")

    

dispatcher.addTelegramCommandHandler('start', start)
dispatcher.addTelegramCommandHandler('createcharacter', createCharacter)
dispatcher.addUnknownTelegramCommandHandler(unknown)                

updater.start_polling()
