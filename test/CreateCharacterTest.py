from telegram import *

updater = Updater(token="INSERT YOUR TOKEN HERE")
dispatcher = updater.dispatcher

characterlist = []
playerIndex = 0

class Character(object):
    playername = None
    charactername = None
    race = None
    _class = None
    stats = {}
    def __init__(self, playername, charactername):
        self.playername = playername
        self.charactername = charactername

def start(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = "Welcome to Dungeons and Dragons.")

def createCharacter(bot, update):
    global playerIndex
    charactername = update.message.text[17:]
    playername = update.message.from_user.first_name
    characterlist.append(Character(playername, charactername))
    bot.sendMessage(chat_id = update.message.chat_id, text = "Character " + characterlist[playerIndex].charactername + " has been created by " + characterlist[playerIndex].playername)
    playerIndex += 1
    defineAttributes(bot, update)

def defineAttributes(bot, update):
    attributesKeyboard = [
        ['Race'],
        ['Class'],
        ['Done!']
    ]
    replyAttributes = telegram.ReplyKeyboardMarkup(attributesKeyboard)
    bot.sendMessage(chat_id = update.message.chat_id, text= "SDefine your character's attributes", reply_markup=replyAttributes)

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
