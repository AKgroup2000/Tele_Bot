import telebot
from telebot import types

import configparser as cfg
file='config.cfg'
parser = cfg.ConfigParser()
parser.read(file)
token = parser.get('creds', 'token')
print(type(token))


bot = telebot.TeleBot(token, parse_mode=None)
chat_id =740871862

# or add KeyboardButton one row at a time:
markup = types.ReplyKeyboardMarkup()
itembtna = types.KeyboardButton('/Mobile')
itembtnv = types.KeyboardButton('/Feature')
#itembtnc = types.KeyboardButton('/PC')
itembtnd = types.KeyboardButton('/Offer')
#itembtne = types.KeyboardButton('/Sale')
markup.row(itembtna, itembtnv, itembtnd)
#markup.row(itembtnc, itembtnd, itembtne)
#bot.send_message(chat_id, "Choose one Option:", reply_markup=markup)
#text="This is a simple text data for testing."
#bot.send_message(chat_id, text)


@bot.message_handler(commands=['Mobile'])
def send_welcome(message):
	bot.reply_to(message, "Mobile Sction")
@bot.message_handler(commands=['Offer'])
def send_welcome(message):
		bot.reply_to(message, "Offer Sction")
@bot.message_handler(commands=['Feature'])
def send_welcome(message):
		bot.reply_to(message, "Features Sction")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, "*** ERROR ***")

bot.polling()
'''

import telebot
import configparser as cfg
file='config.cfg'
parser = cfg.ConfigParser()
parser.read(file)
token = parser.get('creds', 'token')
print(type(token))


bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['Mobile', 'Offer', 'start'])
def send_welcome(message):
		bot.reply_to(message, "Welcome to Chatbot START")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
'''
