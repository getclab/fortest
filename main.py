import telebot
import requests
from bs4 import BeautifulSoup


TOKEN = '1779694450:AAHrawLv8U5ccJxZnnBe_kFyV561EqXKBi0'
bot = telebot.TeleBot(TOKEN, 'HTML')

@bot.message_handler(commands=['start'])
def start(message):
    key = telebot.types.ReplyKeyboardMarkup(True)
    key.add('item')
    bot.send_message(message.chat.id, text='connect', reply_markup=key)

bot.polling()