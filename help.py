from telegram import *

updater = Updater(token="152501487:AAElGigfjuICcLgXT4U2qu74OQyxmjQQ8Ho")
dispatcher = updater.dispatcher

def Help(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = "I am the Dungeons and Dragons bot, and I can help to automate a few processes in DnD to make it easier for everyone to play on Telegram." +
    "\n Here are a list of commands that I can execute!" +
    "\n \n Player Commands:" +
    "\n /start - starts the DnD bot" +
    "\n /createcharacter [character name] - Use this command and follow the prompts to create a new character" +
    "\n /printcharacterstats [character name] - prints a character's stats, add the name of the chharacter after the command" +
    "\n /help - open this help message" +
    "\n \n Dungeon Master Commands:" +
    "\n /createmonster [monster name] [health points] - creates a monster" +
    "\n /attackmonster [monster name] [damage] - reduces health of the monster by a given number" )

dispatcher.addTelegramCommandHandler('help', Help)
       
updater.start_polling()
