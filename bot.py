
"""

University Parser - Парсер ВУЗов (Telegram Bot) - https://t.me/UnivParseBot 
Creator - kudras3r (https://t.me/kudras3r_dev)
Licence - COPYRIGHT ECHO'S DEVELOPMENT © 2023 
All rights reserved

"""


# Imports
import telebot
import json
import os


from groups import links, channels_id
from config import *
from telebot import types
from parse import get_data, xlsx_data
from random import choice
from languages_config import * 


bot = telebot.TeleBot(TOKEN) 


print('Parser has been successfully launched')    # console control


# Info message wait
@bot.message_handler(commands=['info'])
def info(message):
    '''
        Info about dev
    '''
    bot.send_message(message.chat.id, text=LANGUAGES['INFO'],
                     parse_mode="html")

# Start/Language message wait
@bot.message_handler(commands=['start', 'language'])
def start(message):
    '''
        Сhecks the subscription status and give user choice of language
    '''
    
    global non_sub     # In config.py, default == True

    # Take sub status
    for id in channels_id:

        # Subscribe status    
        stat = bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id).status  
            
        if ((stat == "member") or (stat == "creator") or (stat == "administrator")):                
            non_sub = False              
        else:               
            non_sub = True   
    
    markup = types.InlineKeyboardMarkup()
    
    ru = types.InlineKeyboardButton(text='🇷🇺 RU', callback_data='ru')
    eng = types.InlineKeyboardButton(text='🇺🇸 ENG', callback_data='eng')

    markup.add(ru, eng)
    
    bot.send_message(message.from_user.id, text="<b>Выбери язык/Choose your language:</b>", parse_mode="html", reply_markup=markup)

# Languages handler
@bot.callback_query_handler(func = lambda call: call.data in ['ru', 'eng'])
def language(call):
    '''
        Language selection function.
        RUS or ENG - appended at global 'user_language' variable in config.py
    '''
    
    global user_language

    # RUS
    if call.data == "ru":
        
        user_language = 'RUS' 
        
        # Check sub status and let parser work only for subs
        if non_sub == True:
            
            markup = types.InlineKeyboardMarkup()  
            
            for link in links:   
                btn = types.InlineKeyboardButton(text="Подписаться", url=link)
                markup.add(btn)
            
            sub = types.InlineKeyboardButton(text="Я подписался ✅", callback_data='checksub')   
            markup.add(sub)    
            
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f"<b>Привет, {call.message.chat.first_name}!{LANGUAGES['RUS']['sub_request_message_rus']}",
                                  parse_mode="html", reply_markup=markup)
        else:
            markup = types.InlineKeyboardMarkup()
            btn = types.InlineKeyboardButton(text='Продолжить', callback_data='checksub')
            markup.add(btn)
            bot.send_message(chat_id=call.message.chat.id, text='Язык выбран', reply_markup=markup)


    #ENG
    elif call.data == 'eng':
        
        user_language = 'ENG'

        if non_sub == True:
            markup = types.InlineKeyboardMarkup()  
            
            for link in links:   
    
                btn = types.InlineKeyboardButton(text="Subscribe", url=link)
                markup.add(btn)
            
            sub = types.InlineKeyboardButton(text="I subscribed ✅", callback_data='checksub')   
            markup.add(sub)    
            
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f"<b>Hi, {call.message.chat.first_name}!{LANGUAGES['ENG']['sub_request_message_eng']}",
                                  parse_mode="html", reply_markup=markup)
        else:
            markup = types.InlineKeyboardMarkup()
            btn = types.InlineKeyboardButton(text='Continue', callback_data='checksub')
            markup.add(btn)
            bot.send_message(chat_id=call.message.chat.id, text='Successfully', reply_markup=markup)


# Subscribe check
@bot.callback_query_handler(func = lambda call: call.data == 'checksub')
def check_subscribe(call):
    '''
        Subscribe check function. 
        If user is unsub - access to the parser is not given.
        Else - user can use parser.
    '''

    # In groups.py - list with tg group id which user need to subscribe
    for id in channels_id:

        # Subscribe status    
        stat = bot.get_chat_member(chat_id=call.message.chat.id, user_id=call.from_user.id).status  
            
        if ((stat == "member") or (stat == "creator") or (stat == "administrator")):                
            non_sub = False              
        else:               
            non_sub = True 
    
    # If user is sub - go parser
    if non_sub == False:
        
        hello_stic = choice(stics_list)    # just a greeting sticker
        
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton(text='Go parse 👁‍🗨',
                                         callback_data='parse')
        markup.add(btn)
        bot.send_sticker(call.message.chat.id, sticker=hello_stic)
        
        # RUS
        if user_language == 'RUS':
            bot.send_message(chat_id=call.message.chat.id,
                             text=f'<b>Привет, </b>{call.message.chat.first_name}! 👾\n' + LANGUAGES['RUS']['first_message_from_bot_rus'],
                             parse_mode='html',
                             reply_markup=markup)
        # ENG
        elif user_language == 'ENG':
            bot.send_message(chat_id=call.message.chat.id,
                             text=f'<b>HI, </b>{call.message.chat.first_name}! 👾\n' + LANGUAGES['ENG']['first_message_from_bot_eng'],
                             parse_mode='html',
                             reply_markup=markup)
    
    # Else - repeat message about subscribe
    else:
        # RUS
        if user_language == 'RUS':
        
            markup = types.InlineKeyboardMarkup()    
        
            for link in links:    
                btn = types.InlineKeyboardButton(text="Подписаться", url=link)
                markup.add(btn)
        
            sub = types.InlineKeyboardButton(text="Я подписался ✅", callback_data="checksub")   
            markup.add(sub)    
            bot.send_message(call.from_user.id,
                             text="<b>Вы не подписались!\n\nПользоваться ботом можно только после подписки.</b>",
                             parse_mode="html", reply_markup=markup) 
        # ENG
        elif user_language == 'ENG':
        
            markup = types.InlineKeyboardMarkup()    
        
            for link in links:    
                btn = types.InlineKeyboardButton(text="Subscribe", url=link)
                markup.add(btn)
        
            sub = types.InlineKeyboardButton(text="I subscribed ✅", callback_data="checksub")   
            markup.add(sub)    
            bot.send_message(call.from_user.id,
                             text="<b>You have not subscribed!\n\nYou can use the bot only after you subscribe.</b>",
                             parse_mode="html", reply_markup=markup)


# city ​​selection buttons
@bot.callback_query_handler(func = lambda call: call.data == 'parse')
def cities(call):


    ''' 
        The function displays inline buttons so that the user selects a city 
    '''

    if call.message:
        if call.data == 'parse':
            
            for id in channels_id:
        
                # Subscribe status    
                stat = bot.get_chat_member(chat_id=call.message.chat.id, user_id=call.from_user.id).status  
                    
                if ((stat == "member") or (stat == "creator") or (stat == "administrator")):                
                    non_sub = False              
                else:               
                    non_sub = True 
            
            if non_sub == False:

                markup = types.InlineKeyboardMarkup(row_width = 2)
                
                '''Displaying inline buttons with cities >'''
                # RUS
                if user_language == 'RUS':
                    for city in CITIES_RUS.keys():
                        btn = types.InlineKeyboardButton(text=city,
                                                         callback_data=CITIES_RUS[city])
                        markup.add(btn)
                    bot.send_message(call.message.chat.id,
                                    text='Выбери город  >>>',
                                    reply_markup=markup).message_id 
                # ENG
                elif user_language == 'ENG':        
                    for city in CITIES_ENG.keys():
                        btn = types.InlineKeyboardButton(text=city,
                                                         callback_data=CITIES_ENG[city])
                        markup.add(btn)
                    bot.send_message(call.message.chat.id,
                                    text='Choose a city for parse universities >>>',
                                    reply_markup=markup).message_id

            else:
                # RUS
                if user_language == 'RUS':
                
                    markup = types.InlineKeyboardMarkup()    
                
                    for link in links:    
                        btn = types.InlineKeyboardButton(text="Подписаться", url=link)
                        markup.add(btn)
                
                    sub = types.InlineKeyboardButton(text="Я подписался ✅", callback_data="checksub")   
                    markup.add(sub)    
                    bot.send_message(call.from_user.id,
                                     text="<b>Вы не подписались!\n\nПользоваться ботом можно только после подписки.</b>",
                                     parse_mode="html", reply_markup=markup) 
                # ENG
                elif user_language == 'ENG':
                
                    markup = types.InlineKeyboardMarkup()    
                
                    for link in links:    
                        btn = types.InlineKeyboardButton(text="Subscribe", url=link)
                        markup.add(btn)
                
                    sub = types.InlineKeyboardButton(text="I subscribed ✅", callback_data="checksub")   
                    markup.add(sub)    
                    bot.send_message(call.from_user.id,
                                     text="<b>You have not subscribed!\n\nYou can use the bot only after you subscribe.</b>",
                                     parse_mode="html", reply_markup=markup)

                                         
# city ​​tracking
@bot.callback_query_handler(func = lambda call: call.data in CITIES_RUS.values())
def cities_handler(call):

    ''' 
        In response to the choice of the city, 
        this function prompts the user to select a program using the same inline buttons
        and deletes the last message so as not to clog the chat.
        + back button 
    '''
    
    if call.message:
        if call.data in CITIES_RUS.values():
            # RUS
            if user_language == 'RUS':
                # Remember the user city choose
                if call.data not in us_cfg:   
                    us_cfg[0] = call.data.lower()
                # And show him buttons with study programs
                markup = types.InlineKeyboardMarkup(row_width = 2)
                for program in PROGRAMS_RUS.keys():
                    btn = types.InlineKeyboardButton(text=program,
                                                     callback_data=PROGRAMS_RUS[program])
                    markup.add(btn)
                # Back button 
                back_to_cities_btn = types.InlineKeyboardButton(text='Назад ⬅',
                                                                callback_data='back_ct')
                markup.add(back_to_cities_btn)
                bot.send_message(call.message.chat.id,
                                text='Выбери программу обучения',
                                reply_markup=markup)
            # ENG
            elif user_language == 'ENG':
                # Remember the user city choose
                if call.data not in us_cfg:   
                    us_cfg[0] = call.data.lower()
                # And show him buttons with study programs          
                markup = types.InlineKeyboardMarkup(row_width = 2)
                for program in PROGRAMS_ENG.keys():
                    btn = types.InlineKeyboardButton(text=program,
                                                     callback_data=PROGRAMS_ENG[program])
                    markup.add(btn)
                # Back button
                back_to_cities_btn = types.InlineKeyboardButton(text='Back ⬅',
                                                                callback_data='back_ct')
                markup.add(back_to_cities_btn)
                bot.send_message(call.message.chat.id,
                                text='Choose study program',
                                reply_markup=markup)                                                                  
            
            bot.delete_message(call.message.chat.id, call.message.message_id)

# study program ​​tracking
@bot.callback_query_handler(func = lambda call: call.data in PROGRAMS_RUS.values())
def program_handler(call):

    '''
        In response to the choice of the program - 
        inline buttons are placed to select the file format.
        + back button
    '''

    if call.message:
        if call.data in PROGRAMS_RUS.values():
            
            # Saving the selected study program
            if call.data not in us_cfg:
                us_cfg[1] = call.data.lower()
            
            # Placement of buttons for selecting a file format
            markup = types.InlineKeyboardMarkup(row_width = 2)            
            json_btn = types.InlineKeyboardButton(text='JSON',
                                                  callback_data='json')
            xlsx_btn = types.InlineKeyboardButton(text='XLSX',
                                                  callback_data='xlsx')                                            
            markup.add(json_btn, xlsx_btn)
            
            # RUS
            if user_language == 'RUS':
                # Back button
                back_to_progs_btn = types.InlineKeyboardButton(text='Назад ⬅',
                                                               callback_data='back_prog')
                markup.add(back_to_progs_btn)
                bot.send_message(call.message.chat.id,
                                text='Отлично! Выбери формат файла.',
                                reply_markup=markup)
            # ENG
            elif user_language == 'ENG':
                # Back button
                back_to_progs_btn = types.InlineKeyboardButton(text='Back ⬅',
                                                               callback_data='back_prog')
                markup.add(back_to_progs_btn)    
                bot.send_message(call.message.chat.id,
                                text='Nice! Now select file format.',
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
            
            # RUS
            if user_language == 'RUS':
                bot.send_message(call.message.chat.id,
                                 text='Ожидайте...Создание файла может занять несколько минут🕒')
            # ENG
            elif user_language == 'ENG':
                bot.send_message(call.message.chat.id,
                                 text='Waiting...🕒')
            
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
                
                bot.send_document(call.message.chat.id,             # file sending
                                  document=document,
                                  visible_file_name=file_name)
                document.close()
                os.remove(file_name)    # file remove 
                         
            
            # JSON
            elif format == 'json':
                file_name = f'{city}_result_{program[1:-1]}.json'
                file = open(file_name, 'w', encoding='utf-8')
                json.dump(data, file, indent=4, ensure_ascii=False)       
                file.close()

                document = open(file_name, 'rb')

                bot.send_document(call.message.chat.id,             # file sending
                                  document=document,
                                  visible_file_name=file_name)
                document.close()
                os.remove(file_name)   # file remove 

            # RUS
            if user_language == 'RUS':
                button = types.InlineKeyboardMarkup()
                btn = types.InlineKeyboardButton(text='Повторить', callback_data='parse')
                button.add(btn)
                bot.send_message(call.message.chat.id,
                                 text='Ваш файл готов 💾\n/start - заново\n/info - информация\n/language - выбор языка', reply_markup=button)
            # ENG
            elif user_language == 'ENG':
                button = types.InlineKeyboardMarkup()
                btn = types.InlineKeyboardButton(text='Repeat', callback_data='parse')
                button.add(btn)
                bot.send_message(call.message.chat.id,
                                 text='Your file created 💾\n/start - repeat\n/info - information\n/language - language', reply_markup=button)

            bot.delete_message(call.message.chat.id, call.message.message_id)
      
# back buttons response
@bot.callback_query_handler(func = lambda call: call.data in ['back_ct', 'back_prog'])
def back_buttons_handler(call):
    
    if call.message:
        if call.data in ['back_ct']:
            markup = types.InlineKeyboardMarkup(row_width = 2)    
            
            # RUS
            if user_language == 'RUS':
                for city in CITIES_RUS.keys():
                    btn = types.InlineKeyboardButton(text=city,
                                                     callback_data=CITIES_RUS[city])
                    markup.add(btn)
                bot.send_message(call.message.chat.id,
                                text='Выбери город',
                                reply_markup=markup).message_id 
            # ENG
            elif user_language == 'ENG':
                for city in CITIES_ENG.keys():
                    btn = types.InlineKeyboardButton(text=city,
                                                     callback_data=CITIES_ENG[city])
                    markup.add(btn)
                bot.send_message(call.message.chat.id,
                                text='Choose city',
                                reply_markup=markup).message_id 
            
            bot.delete_message(call.message.chat.id, call.message.message_id) 
        
        if call.data in ['back_prog']:
            markup = types.InlineKeyboardMarkup(row_width = 2)

            # RUS
            if user_language == 'RUS':
                for program in PROGRAMS_RUS.keys():
                    btn = types.InlineKeyboardButton(text=program,
                                                     callback_data=PROGRAMS_RUS[program])
                    markup.add(btn)
                back_to_cities_btn = types.InlineKeyboardButton(text='Назад ⬅',
                                                                callback_data='back_ct')
                markup.add(back_to_cities_btn)
                bot.send_message(call.message.chat.id,
                                text='Выбери программу обучения',
                                reply_markup=markup) 
            # ENG
            elif user_language == 'ENG':
                for program in PROGRAMS_ENG.keys():
                    btn = types.InlineKeyboardButton(text=program,
                                                     callback_data=PROGRAMS_ENG[program])
                    markup.add(btn)
                back_to_cities_btn = types.InlineKeyboardButton(text='Назад ⬅',
                                                                callback_data='back_ct')
                markup.add(back_to_cities_btn)
                bot.send_message(call.message.chat.id,
                                text='Choose study program',
                                reply_markup=markup)
            
            bot.delete_message(call.message.chat.id, call.message.message_id)            

# Run
bot.infinity_polling()
