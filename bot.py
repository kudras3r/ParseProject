# This code just connects parser and tg 

import telebot
import json
from config import TOKEN, first_message_from_bot, CITIES
from telebot import types
from parse import get_data


bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn = types.KeyboardButton('Go parse 👁‍🗨')
    markup.add(btn)

    bot.send_message(chat_id=message.chat.id, text=f'<b>HI, </b>{message.chat.first_name}! 👾\n'+first_message_from_bot, parse_mode='html', reply_markup=markup)
    
    

@bot.message_handler(regexp='Go parse 👁‍🗨')
def buttons(message):
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    
    for city in CITIES.keys():
        btn = types.KeyboardButton(city)
        markup.add(btn)

    bot.send_message(message.chat.id, text='Choose city ⌨️', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def return_result(message):


    if message.text in CITIES.keys():

        bot.send_message(message.chat.id, text='Waiting...')
        
        user_URL = f'https://{CITIES[message.text].lower()}.postupi.online/programmy-obucheniya/bakalavr/razdel-matematika-informacionnye-nauki-i-tehnologii/?utm_source=postupi.online&utm_medium=referral&utm_campaign=postupi.online&utm_referrer=postupi.online'
        data = get_data(user_URL)

        with open(f'{message.text}_result.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        with open(f'{message.text}_result.json', 'r', encoding='utf-8') as file:
            bot.send_document(message.chat.id, document=file)
              
        bot.send_message(message.chat.id, text='Here is your file motherfucker!💩')

    else:
        bot.send_message(message.chat.id, text='bro ne tot gorod ti napisal')


bot.polling()