# Imports

import telebot
import json
from config import TOKEN, first_message_from_bot, CITIES, URL
from telebot import types
from parse import get_data, xlsx_data

bot = telebot.TeleBot(TOKEN)

# First message from bot
@bot.message_handler(commands=['start', 'help', 'menu'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='Go parse 👁‍🗨',
                                     callback_data='parse')
    markup.add(btn)
    
    

    with open('univ_photo.png', 'rb') as file:
        photo = file.read()
    bot.send_photo(chat_id=message.chat.id,
                   photo=photo)
    bot.send_message(chat_id=message.chat.id,
                     text=f'<b>HI, </b>{message.chat.first_name}! 👾\n' + "➖\nYou have launched the university parser.\nPlease press  <b>'Go parse 👁‍🗨'</b> and select the city by which universities will be searched.\n➖\nThe result will be send you in <b>'json' or 'xlsx'</b> file",
                     parse_mode='html',
                     reply_markup=markup)


# Tracking callback parse and displaying 2 buttons with file formats
@bot.callback_query_handler(func = lambda call: call.data == 'parse')
def show_file_types(call):
    
    if call.message:
        if call.data == 'parse':                
            
            markup = types.InlineKeyboardMarkup(row_width = 2)

            json_btn = types.InlineKeyboardButton(text='JSON', callback_data='json')
            xlsx_btn = types.InlineKeyboardButton(text='XLSX', callback_data='xlsx')
            
            markup.add(json_btn, xlsx_btn)

            bot.send_message(call.message.chat.id,
                             text='Nice! Now select file format!',
                             reply_markup=markup)
        

# Tracking callback json and displaying buttons with cities
@bot.callback_query_handler(func = lambda call: call.data == 'json')
def json_format(call):

    if call.message:
        if call.data == 'json':
            
            cities_list_json = [f'{city}_json' for city in CITIES.keys()]
            
            markup = types.InlineKeyboardMarkup(row_width = 2)
            
            for city in cities_list_json:
                btn = types.InlineKeyboardButton(text=city.replace('_json', ''),
                                                 callback_data=city)
                markup.add(btn)

            bot.send_message(call.message.chat.id,
                             text='Choose city',
                             reply_markup=markup)

# Tracking callback with the user's city, creating a JSON file and sending it
@bot.callback_query_handler(func = lambda call: call.data in [f'{city}_json' for city in CITIES.keys()])
def json_return(call):

    if call.message:

        json_cities = [f'{city}_json' for city in CITIES.keys()]

        if call.data in json_cities:

            bot.send_message(call.message.chat.id,
                             text='Waiting please...🕒')
            
            user_city = CITIES[call.data.replace('_json', '')]
            url = f'https://{user_city.lower()}.postupi.online/programmy-obucheniya/bakalavr/razdel-matematika-informacionnye-nauki-i-tehnologii/?utm_source=postupi.online&utm_medium=referral&utm_campaign=postupi.online&utm_referrer=postupi.online'

            data = get_data(url)

            ''' Creating JSON'''
            with open(f'{user_city}_result.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            '''Send JSON'''
            with open(f'{user_city}_result.json', 'rb') as file:
                document = file.read()
            
            bot.send_document(call.message.chat.id,
                              document=document,
                              visible_file_name=f'{user_city}_result.json')
            bot.send_message(call.message.chat.id,
                             text='Take your json file dude 💾')



# Tracking callback xlsx and displaying buttons with cities
@bot.callback_query_handler(func = lambda call: call.data == 'xlsx')
def xlsx_format(call):
    
    if call.message:
        if call.data == 'xlsx':

            cities_list_xlsx = [f'{city}_xlsx' for city in CITIES.keys()]

            markup = types.InlineKeyboardMarkup(row_width = 2)

            for city in cities_list_xlsx:
                btn = types.InlineKeyboardButton(text=city.replace('_xlsx', ''),
                                                 callback_data=city)
                markup.add(btn)
            
            bot.send_message(call.message.chat.id,
                             text='Choose city',
                             reply_markup=markup)

# Tracking callback with the user's city, creating a XLSX file and sending it
@bot.callback_query_handler(func = lambda call: call.data in [f'{city}_xlsx' for city in CITIES.keys()])
def xlsx_return(call):
     
    if call.message:

        xlsx_cities = [f'{city}_xlsx' for city in CITIES.keys()]

        if call.data in xlsx_cities:

            bot.send_message(call.message.chat.id, text='Waiting please...🕒')

            ''' Creating URL for request'''
            user_city = CITIES[call.data.replace('_xlsx', '')]
            url = f'https://{user_city.lower()}.postupi.online/programmy-obucheniya/bakalavr/razdel-matematika-informacionnye-nauki-i-tehnologii/?utm_source=postupi.online&utm_medium=referral&utm_campaign=postupi.online&utm_referrer=postupi.online'

            data = get_data(url)
            xlsx_data(data, user_city)

            '''Send XLSX'''
            with open(f'{user_city}_result.xlsx', 'rb') as file:
                document = file.read()
            
            bot.send_document(call.message.chat.id,
                              document=document,
                              visible_file_name=f'{user_city}_result.xlsx')
            bot.send_message(call.message.chat.id,
                             text='Take your xlsx file dude 💾')
   

bot.infinity_polling()

