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
    stats = {'strength': 0, 'dexterity': 0, 'wisdom': 0, "intelligence": 0, "constitution": 0, "charisma": 0}
    inventory = {}
    def __init__(self, playerName, characterName):
        self.playerName = playerName
        self.characterName = characterName

    def updateStats(self, race, _class):
        print ("works!")
        if self.race == 'human':
            self.stats['strength'] = 5
            self.stats['dexterity'] = 5
            self.stats['wisdom'] = 5
            self.stats['intelligence'] = 5
            self.stats['constitution'] = 5
            self.stats['charisma'] = 5
        elif self.race == 'dwarf':
            self.stats['strength'] = 6
            self.stats['dexterity'] = 3
            self.stats['wisdom'] = 3
            self.stats['intelligence'] = 3
            self.stats['constitution'] = 7
            self.stats['charisma'] = 3
        elif self.race == 'elf':
            self.stats['strength'] = 3
            self.stats['dexterity'] = 3
            self.stats['wisdom'] = 8
            self.stats['intelligence'] = 7
            self.stats['constitution'] = 3
            self.stats['charisma'] = 6
        elif self.race == 'ogre':
            self.stats['strength'] = 10
            self.stats['dexterity'] = 3
            self.stats['wisdom'] = 3
            self.stats['intelligence'] = 3
            self.stats['constitution'] = 8
            self.stats['charisma'] = 3
        elif self.race == 'merman':
            self.stats['strength'] = 7
            self.stats['dexterity'] = 5
            self.stats['wisdom'] = 6
            self.stats['intelligence'] = 5
            self.stats['constitution'] = 4
            self.stats['charisma'] = 3
        
        if self._class == 'fighter':
            self.stats['strength'] = self.stats['strength'] + 4
            self.stats['dexterity'] = self.stats['dexterity'] 
            self.stats['wisdom'] = self.stats['wisdom'] - 1
            self.stats['intelligence'] = self.stats['intelligence'] - 2
            self.stats['constitution'] = self.stats['constitution']
            self.stats['charisma'] = self.stats['charisma'] - 1
        elif self._class == 'mage':
            self.stats['strength'] = self.stats['strength'] - 2
            self.stats['dexterity'] = self.stats['dexterity'] + 1
            self.stats['wisdom'] = self.stats['wisdom'] + 1
            self.stats['intelligence'] = self.stats['intelligence'] + 2
            self.stats['constitution'] = self.stats['constitution'] - 2
            self.stats['charisma'] = self.stats['charisma']
        elif self._class == 'thief':
            self.stats['strength'] = self.stats['strength'] - 1
            self.stats['dexterity'] = self.stats['dexterity'] + 2
            self.stats['wisdom'] = self.stats['wisdom'] - 2
            self.stats['intelligence'] = self.stats['intelligence'] 
            self.stats['constitution'] = self.stats['constitution'] - 1
            self.stats['charisma'] = self.stats['charisma'] + 2
        elif self._class == 'priest':
            self.stats['strength'] = self.stats['strength'] - 2
            self.stats['dexterity'] = self.stats['dexterity'] 
            self.stats['wisdom'] = self.stats['wisdom'] + 3
            self.stats['intelligence'] = self.stats['intelligence'] + 1
            self.stats['constitution'] = self.stats['constitution'] - 1
            self.stats['charisma'] = self.stats['charisma'] - 1
            self.stats['gold'] = 250
        elif self._class == 'ranger':
            self.stats['strength'] = self.stats['strength'] - 1
            self.stats['dexterity'] = self.stats['dexterity'] + 3
            self.stats['wisdom'] = self.stats['wisdom'] -1
            self.stats['intelligence'] = self.stats['intelligence'] 
            self.stats['constitution'] = self.stats['constitution'] -2
            self.stats['charisma'] = self.stats['charisma'] + 1
            self.stats['gold'] = 200
        print(str(self.stats))      

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
    print(str(attributes))

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
        characterList[i].updateStats(characterList[i].race, characterList[i]._class)
        printCharacterStats(bot, update)
        attributes = False

def printCharacterStats(bot, update):
    print("hello")
    i = findCharacterIndex(update.message.from_user.first_name)
    text = str(characterList[i].characterName) + "\n Created by: " + str(characterList[i].playerName) + "\n Strength: " + str(characterList[i].stats['strength']) + "\n Dexterity: " + str(characterList[i].stats['dexterity']) + "\n Wisdom: " + str(characterList[i].stats['wisdom']) + "\n Intelligence: " + str(characterList[i].stats['intelligence']) + "\n Constitution: " + str(characterList[i].stats['constitution']) + "\n Charisma: " + str(characterList[i].stats['charisma'])
    print("lol")
    print(text)
    bot.sendMessage(chat_id = update.message.chat_id, text = text) 

def inventoryUpdate(bot, update):
    print ('haha')
    inventoryInput = update.message.text
    inventoryInput = inventoryInput.split()
    i = findCharacterIndex(update.message.from_user.first_name)
    print ('lols')
    if inventoryInput[1] == "remove":
        print ('remove')
        if inventoryInput[2] not in characterList[i].inventory:
            bot.sendMessage(chat_id = update.message.chat_id, text = "@" + characterList[i].playerName + " You don't have %s in your inventory!" % (inventoryInput[2]))
        elif inventoryInput[2] in characterList[i].inventory:
            if int(inventoryInput[3]) > characterList[i].inventory[inventoryInput[2]]:
                print ("not enough!")
                bot.sendMessage(chat_id = update.message.chat_id, text = "@" + characterList[i].playerName + " You don't have enough " + inventoryInput[2] + "!")
            elif int(inventoryInput[3]) == characterList[i].inventory[inventoryInput[2]]:
                del characterList[i].inventory[inventoryInput[2]]
                print ('removed!')
            elif int(inventoryInput[3]) < characterList[i].inventory[inventoryInput[2]]:
                characterList[i].inventory[inventoryInput[2]] = characterList[i].inventory[inventoryInput[2]] - int(inventoryInput[3])
                print ('removed!')
    elif inventoryInput[1] == "add":
        print ('add')
        if inventoryInput[2] not in characterList[i].inventory:
            characterList[i].inventory[inventoryInput[2]] = int(inventoryInput[3])
            print ('added!')
        elif inventoryInput[2] in characterList[i].inventory:
            print ('it\'s in here!')
            characterList[i].inventory[inventoryInput[2]] = characterList[i].inventory[inventoryInput[2]] + int(inventoryInput[3])
            print ('added! :D')
    print (characterList[i].inventory)
    bot.sendMessage(chat_id = update.message.chat_id, text = "@" + characterList[i].playerName + " " + characterList[i].characterName + "\'s Inventory:")
    text
    for key in characterList[i].inventory:
        text += str(key) + ": " + str(characterList[i].inventory[key] + ", ")
    bot.sendMessage(chat_id = update.message.chat_id, text = text)
            

# i = findCharacterIndex(update.message.from_user.first_name)   
def findCharacterIndex(first_name):
    for i in range(len(characterList)):
        if characterList[i].playerName == first_name:
            return i

def unknown(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = "Sorry, I didn't understand that!")

dispatcher.addTelegramMessageHandler(IncomingMessages)
dispatcher.addTelegramCommandHandler('start', start)
dispatcher.addTelegramCommandHandler('createcharacter', createCharacter)
dispatcher.addTelegramCommandHandler('printcharacterstats', printCharacterStats)
dispatcher.addTelegramCommandHandler('inventoryupdate', inventoryUpdate)
dispatcher.addUnknownTelegramCommandHandler(unknown)                

updater.start_polling()
