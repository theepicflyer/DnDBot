from telegram import *

updater = Updater(token="135975691:AAGTcqMOEmgx1pV-laaIRNfkNg8qib00yN8")
dispatcher = updater.dispatcher

def Help(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = "I am the Dungeons and Dragons bot, and I can help to automate a few processes in your game of D&D to make it easier for everyone to play on Telegram." +
    "\n Here are a list of commands that I can execute!" +
    "\n \n Player Commands:" +
    "\n /start - starts the DnD bot" +
    "\n /createcharacter [character name] - Use this command and follow the prompts to create a new character" +
    "\n /printcharacterstats [character name] - Prints a character's stats, add the name of the chharacter after the command" +
    "\n /help - Open this help message" +
    "\n /roll[int] - Rolls a dice with the customisable maximum value"
    "\n \n Dungeon Master Commands:" +
    "\n /createmonster [monster name] [health points] - Creates a monster." +
    "\n /attackmonster [monster name] [damage] - Reduces health of the monster by a given number." +
    "\n /changexp [character name] +/- X - Adds or subtracts a certain amount of health from a character." +
    "\n /changegold [character name] +/- X - Adds or subtracts a certain amount of gold from a character." +
    "\n /changehealth [character name] +/- X - Adds or subtacts a certain amount of health from a character."
    "\n /inventoryupdate [character name] add/remove [item] [no. of item] - Adds or removes a certain amount of a specific item from a character's inventory."
    "\n /printinventory - Current state of the inventory.")
                    

dispatcher.addTelegramCommandHandler('help', Help)
       
updater.start_polling()
                    
