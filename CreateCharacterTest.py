from telegram import *

updater = Updater(token="INSERT YOUR TOKEN HERE")
dispatcher = updater.dispatcher

characterList = []
playerIndex = 0

class Character(object):
    playerName = None
    characterName = None
    race = None
    _class = None
    stats = {}
    def __init__(self, playerName, characterName):
        self.playerName = playerName
        self.characterName = characterName

def start(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = "Welcome to Dungeons and Dragons.")

def createCharacter(bot, update):
    global playerIndex
    characterName = update.message.text[17:]
    playerName = update.message.from_user.first_name
    characterList.append(Character(playerName, characterName))
    bot.sendMessage(chat_id = update.message.chat_id, text = "Character " + characterList[playerIndex].characterName + " has been created by " + characterList[playerIndex].playerName)
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
    for i in characterList:
        if characterList[i].playerName == first_name:
            return i

def unknown(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = "Sorry, I didn't understand that!")

dispatcher.addTelegramCommandHandler('start', start)
dispatcher.addTelegramCommandHandler('createcharacter', createCharacter)
dispatcher.addUnknownTelegramCommandHandler(unknown)                

updater.start_polling()
