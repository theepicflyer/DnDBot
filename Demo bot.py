#Demonstrating some basic stuff with the API
from telegram import Updater
updater = Updater(token='135975691:AAGTcqMOEmgx1pV-laaIRNfkNg8qib00yN8')
dispatcher = updater.dispatcher

#The chat id here is auto generated for every conversation the bot has with a user
#Each user and group the bot communicates with gets a unique id
def start(bot, update): #The below code happens when /start command is called
    bot.sendMessage(chat_id=update.message.chat_id, text="Hello!")
    print("start called")

#These functions are called by the library when the command is detected
#The bot parameter is the bot object that you use to send messages, etc.
#The update parameter contains the new messages since the previous time it was updated by any function
def bye(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Bye :(")
    print("bye called")

def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="You just sent: "
                    +update.message.text) #Concatenating text to the user's message

def message(bot, update):
    date = update.message.date
    print("Message <" + update.message.text + "> sent from <" + update.message.from_user.username + "> at <" + date.minute + "> minutes")

dispatcher.addTelegramCommandHandler('start', start) #Binds /start command to the function
dispatcher.addTelegramCommandHandler('bye', bye)
dispatcher.addTelegramMessageHandler(echo)
dispatcher.addTelegramCommandHandler('return', message)
updater.start_polling() #Keeps checking until stop_polling() is called lols
#this is a comment
