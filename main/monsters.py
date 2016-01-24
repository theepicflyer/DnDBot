from telegram import *

updater = Updater(token="TOKEN")
dispatcher = updater.dispatcher

monsterList = [] #list storing all monsters
monsterIndex = 0 #number of monsters

class Monster(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

def findMonsterIndex(name): #returns index of character using player name
    for i in range(len(monsterList)):
        if name == monsterList[i].name:
            return i

def createMonster(bot, update):
    global monsterIndex
    input = update.message.text #input: /createmonster NAME HEALTH
    input = input.split() #split the input into the 3 parts
    monsterName = input[1]
    health = int(input[2])
    monsterList.append(Monster(monsterName, health)) #add to list
    bot.sendMessage(chat_id = update.message.chat_id, text = monsterList[monsterIndex].name + " has been created with %d health" % (monsterList[monsterIndex].health))
    monsterIndex += 1

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Hello")
    
def attackMonster(bot, update):
    input = update.message.text #input: /attackmonster NAME DAMAGE
    input = input.split() #split into the parts
    i = findMonsterIndex(input[1])
    damage = int(input[2])
    monsterList[i].health -= damage
    bot.sendMessage(chat_id = update.message.chat_id, text = monsterList[i].name + "'s health has reduced by " + str(damage) + " to " + str(monsterList[i].health))
    
dispatcher.addTelegramCommandHandler('createmonster', createMonster)
dispatcher.addTelegramCommandHandler('start', start)
dispatcher.addTelegramCommandHandler('attackmonster', attackMonster)
updater.start_polling()
