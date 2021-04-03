import telebot
import requests
from bs4 import BeautifulSoup


TOKEN = '1779694450:AAHrawLv8U5ccJxZnnBe_kFyV561EqXKBi0'
bot = telebot.TeleBot(TOKEN, 'HTML')



@bot.message_handler(commands=['start'])
def start(message):
    key = telebot.types.ReplyKeyboardMarkup(True)
    key.add('🎵Искать песню🎵')
    bot.send_message(message.chat.id, text=f'Привет {message.chat.first_name}', reply_markup=key)


@bot.message_handler(content_types=['text'])
def music(message):
    if message.text == '🎵Искать песню🎵':
        smg = bot.send_message(message.chat.id, 'Введите название:')
        bot.register_next_step_handler(smg, serq)

def serq(message):
    Q = message.text
    link = f'https://txt-pesen.ru/component/search/?searchword={Q}&ordering=newest&searchphrase=all&limit=50'
    r = requests.get(link).text
    soup = BeautifulSoup(r, 'html.parser')
    block = soup.find_all('dt', class_='result-title')
    for item in block:
        name = item.find('a').text.lstrip()
        bot.send_message(message.chat.id, text=name)

bot.polling()