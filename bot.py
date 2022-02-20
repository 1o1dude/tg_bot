import telebot
from telebot import types


name = ''
surname = ''
age = 0

bot = telebot.TeleBot("5112105842:AAGs0xlJIpYc0x_RcF3OblpnHn5MuwGm__A")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет этот бот создан для ничего, просто так 👋. (с ознокомлением команд пропишите /help)")

@bot.message_handler(commands=['support'])
def send_welcome(message):
    bot.reply_to(message, "Здраствуйте, вы можете связаться с разработчиком Vk- https://vk.com/vadim_gangster007, Discord- king Darvel#5822,GitHub- https://github.com/1o1dude)")

@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.reply_to(message, "Привет, сейчас автор-создатель этого тг бота занимаеться проектом https://github.com/1o1dude/ABOBAbeta вы его можете поддержать переводом денег на номер карты 5228 6005 7292 1718 (сбер/мастер кард)")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Привет 😊, вот мой список команд: /reg, /help,/start,/info,/support")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'Привет':
        bot.reply_to(message, '🤖 привет привет 🤖')
    if message.text == 'привет':
        bot.reply_to(message, '🤖 привет привет 🤖')
    elif message.text == 'hi':
        bot.reply_to(message, 'Hi again!')
    elif message.text == '/reg':
        bot.send_message(message.from_user.id, "Привет,Как тебя зовут? 😨")
        bot.register_next_step_handler(message, reg_name)

    #bot.reply_to(message, message.text)

def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "назови-ка свой ник-нейм 🕹")
    bot.register_next_step_handler(message, reg_surname)

def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "а теперь назови свой возраст 🤔")
    bot.register_next_step_handler(message, reg_age)

def reg_age(message):
    global age
    #age = message.text
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "Вводите цифрами!")

    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Тебе ' + str(age) + ' лет? И тебя зовут: ' + name + ' ' + surname + '?'
    bot.send_message(message.from_user.id, text = question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, "Приятно познакомиться")
    elif call.data == "no":
        bot.send_message(call.message.chat.id, "Попробуем еще раз 🤷‍🥱")
        bot.send_message(call.message.chat.id, "Привет! Как тебя зовут?")
        bot.register_next_step_handler(call.message, reg_name)

bot.polling()
