from twx.botapi import TelegramBot, ReplyKeyboardMarkup

bot = TelegramBot('52501487:AAElGigfjuICcLgXT4U2qu74OQyxmjQQ8Ho')
bot.update_bot_info().wait()
print(bot.username)

keyboard = [
            ['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            ['0']
            ]

reply_markup = ReplyKeyboardMarkup.create(keyboard)

bot.send_message(user_id, 'please enter a number', reply_markup=reply_markup).wait()