#remember checking for race and class

from telegram import *

updater = Updater(token="152501487:AAElGigfjuICcLgXT4U2qu74OQyxmjQQ8Ho")
dispatcher = updater.dispatcher

characterList = []
playerIndex = 0

attributes = False

class Character(object):
    playerName = None
    characterName = None
    race = None
    _class = None
    health = 30
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
    bot.sendMessage(chat_id = update.message.chat_id, text = "@" + playerName + " Please enter your character's attributes in the format: race class")
    global attributes
    attributes = True

def IncomingMessages(bot, update):
    global attributes
    if attributes == True:
        print ("lols")
        attributesInput = update.message.text
        attributesInput = attributesInput.split()
        print (attributesInput[0])
        i = findCharacterIndex(update.message.from_user.first_name)
        characterList[i].race = attributesInput[0]
        characterList[i]._class = attributesInput[1]
        bot.sendMessage(chat_id = update.message.chat_id, text = "@" + characterList[i].playerName + " " + characterList[i].characterName + "'s race and class is " + characterList[i].race + " and " + characterList[i]._class)
        attributes = False

def findCharacterIndex(first_name):
    for i in range(len(characterList)):
        if characterList[i].playerName == first_name:
            return i

def unknown(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = "Sorry, I didn't understand that!")

dispatcher.addTelegramMessageHandler(IncomingMessages)
dispatcher.addTelegramCommandHandler('start', start)
dispatcher.addTelegramCommandHandler('createcharacter', createCharacter)
dispatcher.addUnknownTelegramCommandHandler(unknown)                

updater.start_polling()
