import telebot
import requests
from bs4 import BeautifulSoup


TOKEN = '1779694450:AAHrawLv8U5ccJxZnnBe_kFyV561EqXKBi0'
bot = telebot.TeleBot(TOKEN, 'HTML')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text='connect')

bot.polling()