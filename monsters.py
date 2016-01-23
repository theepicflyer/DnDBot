from telegram import *

updater = Updater(token="146256100:AAF_w7XAU6fU8Zm7TXLA0RMzZE4qjeVzNd0")
dispatcher = updater.dispatcher

monsterlist = []

class Monster(object):
    health = 30
    strength = 5
    def __init__(self, monstername):
        self.monstername = monstername
    def Monstercheckhealth(self):
        bot.sendMessage(chat_id=chat_id, text= self.monstername + "'s is" + self.health)
    def
    

def createMonster(bot,update):
    monstername = update.message.text[15:]
    monsterlist.append(Monster(monstername))
    bot.sendMessage(chat_id = update.message.chat_id, text = monsterlist[0].monstername + "has been created")

def attackMonster(bot, update):
