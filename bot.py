import telebot
from telebot import types

bot = telebot.TeleBot("5112105842:AAGs0xlJIpYc0x_RcF3OblpnHn5MuwGm__A")

name = ''
surname = ''
age = 0


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Вот мой список команд: /help,/start,Привет,/reg")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'Привет':
        bot.reply_to(message, 'Привет, этот бот вам поможет ознакомлением репозитория- https://github.com/1o1dude/ABOBAbeta')
    elif message.text == 'Hello':
        bot.reply_to(message, 'Hi, this is bot helping you with learning a repozitoriy- https://github.com/1o1dude/ABOBAbeta')
    elif message.text == '/reg':
        bot.send_message(message.from_user.id, 'Привет, как тебя зовут?')
        bot.register_next_step_handler(message, reg_name)

def reg_name(message):
    global name
    name = message.text
    bot.send_message (message.from_user.id, 'понятненько, хм.. интересно, напишика свой игровой nick-name')
    bot.register_next_step_handler (message, reg_surname)

def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message (message.from_user.id, 'так, а теперь назови-ка свой возраст')
    bot.register_next_step_handler (message, reg_age)

def reg_age(message):
    global age
    #age = message.text
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message (message.from_user.id, 'Пожалуйста, вводите текст цифрами')
    bot.send_message (message.from_user.id, 'Тебе ' +str(age)+' лет? и тебя зовут ' +str(name)+' и твой ник? '+str(surname))
    keyboard = types.InlineKeyboardMarup()
    key_yes = types.InlineKeyboardMarup(text='Да', callback_data='Yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardMarup (text='Нет', callback_data='No')
    keyboard.add (key_no)


bot.infinity_polling()
