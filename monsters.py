from telegram import *

updater = Updater(token="129193826:AAHfEbo7HjUhk5T48PC6gEhPgsIEYP8iuNI")
dispatcher = updater.dispatcher

monsterList = []
monsterIndex = 0

class Monster(object):
    strength = 5
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    
def monsterStats(bot, update):
    findMonsterIndex(update.message.text[14:])
    
    print (monster)
    print (monster.health)

def findMonsterIndex(name):
    for i in range(len(monsterList)):
        if name == monsterList[i].name:
            return i

def createMonster(bot, update):
    global monsterIndex
    monsterName = update.message.text[15:]
    health = 5
    monsterList.append(Monster(monsterName, health))
    print (monsterList[monsterIndex].name)
    bot.sendMessage(chat_id = update.message.chat_id, text = monsterList[monsterIndex].name + " has been created")
    monsterIndex += 1

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Hello")
    
#def attackMonster(bot, update):

dispatcher.addTelegramCommandHandler('createmonster', createMonster)
dispatcher.addTelegramCommandHandler('monsterstats', monsterStats)
dispatcher.addTelegramCommandHandler('start', start)
#dispatcher.addTelegramCommandHandler('attackmonster', attackMonster)
updater.start_polling()
