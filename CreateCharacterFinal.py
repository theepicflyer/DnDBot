from telegram import *

updater = Updater(token="135975691:AAGTcqMOEmgx1pV-laaIRNfkNg8qib00yN8")
dispatcher = updater.dispatcher

characterList = []
playerIndex = 0

attributes = False

class Character(object):
    playerName = None
    characterName = None
    race = None
    _class = None
    stats = {'strength': 0, 'dexterity': 0, 'wisdom': 0, "intelligence": 0, "constitution": 0, "charisma": 0, "health": 0}
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
            if self.stats ['constitution'] == 5:
                self.stats['health']= 18
        #Race Stats for Dwarf
        elif self.race == 'dwarf':
            self.stats['strength'] = 6
            self.stats['dexterity'] = 3
            self.stats['wisdom'] = 3
            self.stats['intelligence'] = 3
            self.stats['constitution'] = 7
            self.stats['charisma'] = 3
            if self.stats ['constitution'] == 7:
                self.stats['health']= 20
        #Race Stats for Elf
        elif self.race == 'elf':
            self.stats['strength'] = 3
            self.stats['dexterity'] = 3
            self.stats['wisdom'] = 8
            self.stats['intelligence'] = 7
            self.stats['constitution'] = 3
            self.stats['charisma'] = 6
            if self.stats ['constitution'] ==3:
                self.stats['health']= 16
        #Race Stats for Ogre
        elif self.race == 'ogre':
            self.stats['strength'] = 10
            self.stats['dexterity'] = 3
            self.stats['wisdom'] = 3
            self.stats['intelligence'] = 3
            self.stats['constitution'] = 8
            self.stats['charisma'] = 3
            if self.stats ['constitution'] ==8:
                self.stats['health']= 21
        #Race Stats for Merman
        elif self.race == 'merman':
            self.stats['strength'] = 7
            self.stats['dexterity'] = 5
            self.stats['wisdom'] = 6
            self.stats['intelligence'] = 5
            self.stats['constitution'] = 4
            self.stats['charisma'] = 3
            if self.stats ['constitution'] ==4:
                self.stats['health']= 17
        #Class Stats for Fighter
        if self._class == 'fighter':
            self.stats['strength'] = self.stats['strength'] + 2
            self.stats['dexterity'] = self.stats['dexterity'] 
            self.stats['wisdom'] = self.stats['wisdom'] - 1
            self.stats['intelligence'] = self.stats['intelligence'] - 2
            self.stats['constitution'] = self.stats['constitution'] + 2
            self.stats['charisma'] = self.stats['charisma'] - 1
            self.stats['gold'] = 50
        #Class Stats for Mage
        elif self._class == 'mage':
            self.stats['strength'] = self.stats['strength'] - 2
            self.stats['dexterity'] = self.stats['dexterity'] 
            self.stats['wisdom'] = self.stats['wisdom'] + 2
            self.stats['intelligence'] = self.stats['intelligence'] + 2
            self.stats['constitution'] = self.stats['constitution'] - 1
            self.stats['charisma'] = self.stats['charisma'] - 1
            self.stats['gold'] = 100
        #Class Stats for Priest
        elif self._class == 'priest':
            self.stats['strength'] = self.stats['strength'] - 2
            self.stats['dexterity'] = self.stats['dexterity'] 
            self.stats['wisdom'] = self.stats['wisdom'] + 3
            self.stats['intelligence'] = self.stats['intelligence'] + 1
            self.stats['constitution'] = self.stats['constitution'] - 1
            self.stats['charisma'] = self.stats['charisma'] - 1
            self.stats['gold'] = 250
        #Class Stats for Thief
        elif self._class == 'thief':
            self.stats['strength'] = self.stats['strength'] - 1
            self.stats['dexterity'] = self.stats['dexterity'] + 2
            self.stats['wisdom'] = self.stats['wisdom'] -2
            self.stats['intelligence'] = self.stats['intelligence'] 
            self.stats['constitution'] = self.stats['constitution'] -1
            self.stats['charisma'] = self.stats['charisma'] + 2
            self.stats['gold'] = 200
        #Class Stats for Ranger
        elif self._class == 'ranger':
            self.stats['strength'] = self.stats['strength'] - 1
            self.stats['dexterity'] = self.stats['dexterity'] + 3
            self.stats['wisdom'] = self.stats['wisdom'] -1
            self.stats['intelligence'] = self.stats['intelligence'] 
            self.stats['constitution'] = self.stats['constitution'] -2
            self.stats['charisma'] = self.stats['charisma'] + 1
            self.stats['gold'] = 200
            
            def changehealth(bot, update, self):
                bot.sendMessage(chat_id = update.message.chat_id, text = "Add or Subtract Health by Keying it [Subtract/Add] [Number]")
                number = int (update.message.text[2:])
                pos = (update.message.text[1:])
                if (pos[1:] == "S"
                    self.stats['health'] = self.stats['health'] - number
                elif (pos[1:]) == "A"
                    self.stats['health'] = self.stats['health'] + number
              
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
        + "\n Charisma: " + str(characterList[i].stats['charisma'])
        + "\n Health: " + str(characterList[i].stats['health']))
        print(statsheet)
        bot.sendMessage(chat_id = update.message.chat_id, text = statsheet) 
        attributes = False

def printCharacterStats(bot, update):
    # /printcharacterstats CHARACTER_NAME
    _input = update.message.text
    _input = _input.split()
    name = _input[1]
    for i in range(len(characterList)):
        if characterList[i].characterName == name:
            pass
    statsheet = str(characterList[i].characterName) + "\n Created by: " + str(characterList[i].playerName) + "\n Strength: " + str(characterList[i].stats['strength']) + "\n Dexterity: " + str(characterList[i].stats['dexterity']) + "\n Wisdom: " + str(characterList[i].stats['wisdom']) + "\n Intelligence: " + str(characterList[i].stats['intelligence']) + "\n Constitution: " + str(characterList[i].stats['constitution']) + "\n Charisma: " + str(characterList[i].stats['charisma']) + "\n Health: " + str(CharacterList[i].stats['health'])
    bot.sendMessage(chat_id = update.message.chat_id, text = statsheet) 

def findCharacterIndex(first_name):
    for i in range(len(characterList)):
        if characterList[i].playerName == first_name:
            return i

def unknown(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = "Sorry, I didn't understand that!")


dispatcher.addTelegramMessageHandler(incomingMessages)
dispatcher.addTelegramCommandHandler('changehealth', changehealth)
dispatcher.addTelegramCommandHandler('start', start)
dispatcher.addTelegramCommandHandler('createcharacter', createCharacter)
dispatcher.addTelegramCommandHandler('printcharacterstats', printCharacterStats)
dispatcher.addUnknownTelegramCommandHandler(unknown)

updater.start_polling()
