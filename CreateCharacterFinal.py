from telegram import *

updater = Updater(token="")
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
    stats = {'strength': 0, 'dexterity': 0, 'wisdom': 0, "intelligence": 0, "constitution": 0, "charisma": 0}
    def __init__(self, playerName, characterName):
        self.playerName = playerName
        self.characterName = characterName

    def updateStats(self, race, _class):
        #Race Stats for Human
        if self.race == 'human':
            self.stats['strength'] = 5
            self.stats['dexterity'] = 5
            self.stats['wisdom'] = 5
            self.stats['intelligence'] = 5
            self.stats['constitution'] = 5
            self.stats['charisma'] = 5
        #Race Stats for Dwarf
        elif self.race == 'dwarf':
            self.stats['strength'] = 6
            self.stats['dexterity'] = 3
            self.stats['wisdom'] = 3
            self.stats['intelligence'] = 3
            self.stats['constitution'] = 7
            self.stats['charisma'] = 3
        #Race Stats for Elf
        elif self.race == 'elf':
            self.stats['strength'] = 3
            self.stats['dexterity'] = 3
            self.stats['wisdom'] = 8
            self.stats['intelligence'] = 7
            self.stats['constitution'] = 3
            self.stats['charisma'] = 6
        #Class Stats for Fighter
        if self._class == 'fighter':
            self.stats['strength'] = self.stats['strength'] + 4
            self.stats['dexterity'] = self.stats['dexterity'] 
            self.stats['wisdom'] = self.stats['wisdom'] - 1
            self.stats['intelligence'] = self.stats['intelligence'] - 2
            self.stats['constitution'] = self.stats['constitution']
            self.stats['charisma'] = self.stats['charisma'] - 1
        #Class Stats for Mage
        elif self._class == 'mage':
            self.stats['strength'] = self.stats['strength'] - 2
            self.stats['dexterity'] = self.stats['dexterity'] + 1
            self.stats['wisdom'] = self.stats['wisdom'] + 1
            self.stats['intelligence'] = self.stats['intelligence'] + 2
            self.stats['constitution'] = self.stats['constitution'] - 2
            self.stats['charisma'] = self.stats['charisma']
        #Class Stats for Thief
        elif self._class == 'thief':
            self.stats['strength'] = self.stats['strength'] - 1
            self.stats['dexterity'] = self.stats['dexterity'] + 2
            self.stats['wisdom'] = self.stats['wisdom'] - 1
            self.stats['intelligence'] = self.stats['intelligence'] 
            self.stats['constitution'] = self.stats['constitution'] - 2
            self.stats['charisma'] = self.stats['charisma'] + 2     

def start(bot, update):
    #Displays "Welcome to Dungeons and Dragons.")
    bot.sendMessage(chat_id = update.message.chat_id, text = "Welcome to Dungeons and Dragons.")

def createCharacter(bot, update):
    global playerIndex
    characterName = update.message.text[17:]
    playerName = update.message.from_user.first_name
    characterList.append(Character(playerName, characterName))
    #Displays "Character [Character] has been created [Player]"
    bot.sendMessage(chat_id = update.message.chat_id, text = "Character " + characterList[playerIndex].characterName + " has been created by " + characterList[playerIndex].playerName)
    playerIndex += 1
    #Displays "@[Player] Please enter your character's attributes in the format of [Race] [Class]"
    bot.sendMessage(chat_id = update.message.chat_id, text = "@" + playerName + " Please enter your character's Race & Class in the format: [Race] [Class]")
    global attributes
    attributes = True

def incomingMessages(bot, update):
    global attributes
    if attributes == True:
        attributesInput = update.message.text
        attributesInput = attributesInput.split()
        i = findCharacterIndex(update.message.from_user.first_name)
        characterList[i].race = attributesInput[0]
        characterList[i]._class = attributesInput[1]
        #Display "@[Player] [Character]'s race is [Race] and [Character]'s class is [Class]
        bot.sendMessage(chat_id = update.message.chat_id, text = "@" + characterList[i].playerName + " " + characterList[i].characterName + "'s race is " + characterList[i].race + " and " + characterList[i].characterName + "'s class is "+ characterList[i]._class + ".")
        characterList[i].updateStats(characterList[i].race, characterList[i]._class)
        statsheet = (str(characterList[i].characterName) + "\n Created by: "
        + str(characterList[i].playerName)
        + "\n Strength: " + str(characterList[i].stats['strength'])
        + "\n Dexterity: " + str(characterList[i].stats['dexterity'])
        + "\n Wisdom: " + str(characterList[i].stats['wisdom'])
        + "\n Intelligence: " + str(characterList[i].stats['intelligence'])
        + "\n Constitution: " + str(characterList[i].stats['constitution'])
        + "\n Charisma: " + str(characterList[i].stats['charisma']))
        print(statsheet)
        bot.sendMessage(chat_id = update.message.chat_id, text = statsheet) 
        attributes = False

def printCharacterStats(bot, update):
    # /printcharacterstats CHARACTER_NAME
    input = update.message.text
    input = input.split()
    name = input[1]
    for i in range(len(characterList)):
        if characterList[i].characterName == name:
            pass
    statsheet = str(characterList[i].characterName) + "\n Created by: " + str(characterList[i].playerName) + "\n Strength: " + str(characterList[i].stats['strength']) + "\n Dexterity: " + str(characterList[i].stats['dexterity']) + "\n Wisdom: " + str(characterList[i].stats['wisdom']) + "\n Intelligence: " + str(characterList[i].stats['intelligence']) + "\n Constitution: " + str(characterList[i].stats['constitution']) + "\n Charisma: " + str(characterList[i].stats['charisma'])
    bot.sendMessage(chat_id = update.message.chat_id, text = statsheet) 

def findCharacterIndex(first_name):
    for i in range(len(characterList)):
        if characterList[i].playerName == first_name:
            return i

def unknown(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = "Sorry, I didn't understand that!")

dispatcher.addTelegramMessageHandler(incomingMessages)
dispatcher.addTelegramCommandHandler('start', start)
dispatcher.addTelegramCommandHandler('createcharacter', createCharacter)
dispatcher.addTelegramCommandHandler('printcharacterstats', printCharacterStats)
dispatcher.addUnknownTelegramCommandHandler(unknown)

updater.start_polling()
