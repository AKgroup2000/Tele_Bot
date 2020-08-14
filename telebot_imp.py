import telebot
import configparser as cfg
file='config.cfg'
parser = cfg.ConfigParser()
parser.read(file)
token = parser.get('creds', 'token')
print(type(token))

#tocken= '1366726613:AAFxugWdQ46h-BHGjdAuDfW0RVpua4VgibM'
bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['Mobile', 'Offer', 'start'])
def send_welcome(message):
		bot.reply_to(message, "Welcome to Chatbot START")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()

