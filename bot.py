
import telebot
import json

from config import *
from telebot import types
from parse import get_data, xlsx_data
from random import choice


bot = telebot.TeleBot(TOKEN) 

# response to start
@bot.message_handler(commands=['start', 'help', 'menu'])
def send_welcome(message):
    
    hello_stic = choice(stics_list)    # just a greeting sticker
    
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='Go parse 👁‍🗨',
                                     callback_data='parse')
    markup.add(btn)

    bot.send_sticker(message.chat.id, sticker=hello_stic)
    bot.send_message(chat_id=message.chat.id,
                     text=f'<b>HI, </b>{message.chat.first_name}! 👾\n' + first_message_from_bot,
                     parse_mode='html',
                     reply_markup=markup)

# city ​​selection buttons
@bot.callback_query_handler(func = lambda call: call.data == 'parse')
def showing_cities(call):
    
    ''' 
        The function displays inline buttons so that the user selects a city 
    '''
    
    if call.message:
        if call.data == 'parse':

            markup = types.InlineKeyboardMarkup(row_width = 2)

            for city in CITIES.keys():
                btn = types.InlineKeyboardButton(text=city,
                                                 callback_data=city)
                markup.add(btn)     

            bot.send_message(call.message.chat.id,
                            text='Choose a city for parse universities >>>',
                            reply_markup=markup).message_id   
                                         
# city ​​tracking
@bot.callback_query_handler(func = lambda call: call.data in CITIES.keys())
def cities_handler(call):
    
    ''' 
        In response to the choice of the city, 
        this function prompts the user to select a program using the same inline buttons
        and deletes the last message so as not to clog the chat.
        + back button 
    '''
    
    if call.message:
        if call.data in CITIES.keys():

            # saving the selected city  
            if call.data not in us_cfg:   
                us_cfg[0] = CITIES[call.data].lower()
            
            # placement of buttons for selecting a study program
            markup = types.InlineKeyboardMarkup(row_width = 2)
            for program in PROGRAMS.keys():
                btn = types.InlineKeyboardButton(text=program,
                                                 callback_data=program)
                markup.add(btn)
            
            # back button
            back_to_cities_btn = types.InlineKeyboardButton(text='BACK ⬅',
                                                            callback_data='back_ct')
            markup.add(back_to_cities_btn)                                                            
            
            bot.send_message(call.message.chat.id,
                            text='Choose study program',
                            reply_markup=markup)
            bot.delete_message(call.message.chat.id, call.message.message_id)

# study program ​​tracking
@bot.callback_query_handler(func = lambda call: call.data in PROGRAMS.keys())
def program_handler(call):

    '''
        In response to the choice of the program - 
        inline buttons are placed to select the file format.
        + back button
    '''

    if call.message:
        if call.data in PROGRAMS.keys():
            
            # saving the selected study program
            if call.data not in us_cfg:
                us_cfg[1] = PROGRAMS[call.data].lower()
            
            # placement of buttons for selecting a file format
            markup = types.InlineKeyboardMarkup(row_width = 2)            
            json_btn = types.InlineKeyboardButton(text='JSON',
                                                  callback_data='json')
            xlsx_btn = types.InlineKeyboardButton(text='XLSX',
                                                  callback_data='xlsx')                                            
            markup.add(json_btn, xlsx_btn)
            
            # back button
            back_to_progs_btn = types.InlineKeyboardButton(text='BACK ⬅',
                                                           callback_data='back_prog')
            markup.add(back_to_progs_btn)
            
            bot.send_message(call.message.chat.id,
                            text='Nice! Now select file format!',
                            reply_markup=markup)
            bot.delete_message(call.message.chat.id, call.message.message_id)

# file format ​​tracking                    
@bot.callback_query_handler(func = lambda call: call.data in ['json', 'xlsx'])
def format_handler(call):

    '''
        Taking into account the values selected by the user,
        this function returns the final file with the list of universities.
        The file is created in parse.py.
    '''

    if call.message:
        if call.data in ['json', 'xlsx']:

            bot.send_message(call.message.chat.id,
                             text='Waiting please...🕒')
            
            # user values
            format = call.data

            city = us_cfg[0]
            print(f'us_city = {city}')

            program = us_cfg[1]
            print(f'us_program = {program}')             
            
            url = 'https://'+city+URL+program
            print(f'URL = {url}')   
            
            # parse.py work
            data = get_data(url)
            
            # sending file ----
            # XLSX
            if format == 'xlsx':
                file_name = xlsx_data(data, city, program)
                document = open(file_name, 'rb')
                bot.send_document(call.message.chat.id,
                                  document=document,
                                  visible_file_name=file_name)
                bot.send_message(call.message.chat.id,
                                 text='Take your xlsx file dude 💾\nAnd /start to repeat')          
            
            # JSON
            elif format == 'json':
                file_name = f'{city}_result_{program[1:-1]}.json'
                file = open(file_name, 'w', encoding='utf-8')
                json.dump(data, file, indent=4, ensure_ascii=False)       
                file.close()

                document = open(file_name, 'rb')

                bot.send_document(call.message.chat.id,
                                  document=document,
                                  visible_file_name=file_name)
                bot.send_message(call.message.chat.id,
                                 text='Take your json file dude 💾\nAnd /start to repeat')
            
            bot.delete_message(call.message.chat.id, call.message.message_id)
      
# back buttons response
@bot.callback_query_handler(func = lambda call: call.data in ['back_ct', 'back_prog'])
def back_buttons_handler(call):
    
    if call.message:
        if call.data in ['back_ct']:
            markup = types.InlineKeyboardMarkup(row_width = 2)

            for city in CITIES.keys():
                btn = types.InlineKeyboardButton(text=city,
                                                 callback_data=city)
                markup.add(btn)     

            bot.send_message(call.message.chat.id,
                            text='Choose city',
                            reply_markup=markup).message_id 
            bot.delete_message(call.message.chat.id, call.message.message_id) 
        
        if call.data in ['back_prog']:
            markup = types.InlineKeyboardMarkup(row_width = 2)

            for program in PROGRAMS.keys():
                btn = types.InlineKeyboardButton(text=program,
                                                 callback_data=program)
                markup.add(btn)
            back_to_cities_btn = types.InlineKeyboardButton(text='BACK ⬅',
                                                            callback_data='back_ct')
            markup.add(back_to_cities_btn)                                                            
            bot.send_message(call.message.chat.id,
                            text='Choose study program',
                            reply_markup=markup)
            bot.delete_message(call.message.chat.id, call.message.message_id)            

# run
bot.infinity_polling()

