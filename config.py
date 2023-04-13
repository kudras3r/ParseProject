
"""

University Parser - Парсер ВУЗов (Telegram Bot) - https://t.me/UnivParseBot 
Creator - kudras3r (https://t.me/kudras3r_dev)
Licence - COPYRIGHT ECHO'S DEVELOPMENT © 2023 
All rights reserved

"""

from fake_useragent import UserAgent
ua = UserAgent()
random_user_agent = ua.random


# token!
TOKEN = '' 


URL = '.postupi.online/programmy-obucheniya/bakalavr/razdel'

# for bot ----------------------------------------------------------------------------
us_cfg = [0, 0]

stics_list = ['CAACAgIAAxkBAAEGtZ9jj2ueUlsgtjId0_3mh-sDKxemyAAC1hgAAliWUUvKsK_EzGqmJCsE',
              'CAACAgIAAxkBAAEGtVFjj1xJt-hvMaS8yK0UYY2yYUET1QAC1SIAAjrw-EuqVhe4O4uNEysE',
              'CAACAgIAAxkBAAEGtaFjj2vCCeyu88mhILC58xN0Z5fyQwACSBQAAmoz4UlQCUG0FKMZiSsE',
              'CAACAgIAAxkBAAEGtaNjj2vWHPCT2FJfjMLegSLDslJ43gACvxIAAu7r4EvtwiQURMY0dCsE']

# for parser an bot -------------------------------------------------------------------
PROGRAMS_RUS = {
    'Дизайн': '-dizajn/',
    'Маркетинг': '-marketing/',
    'Искусство и культура': '-iskusstvo-i-kultura/',
    'История и археология': '-istoriya-arheologiya-i-dokumentovedenie/',
    'Качество и контроль в технических системах': '-kachestvo-i-upravlenie-v-tehnicheskih-sistemah/',
    'Логистика': '-logistika/',
    'Математика и инф-е технологии': '-matematika-informacionnye-nauki-i-tehnologii/',
    'Машиностроение и робототехника': '-mashinostroenie-avtomatizaciya-i-robototehnika/',
    'Медицина': '-medicina-i-zdravoohranenie/',
    'Химические и биологические науки': '-himiko-biologicheskie-nauki-i-tehnologii/'  
}
PROGRAMS_ENG = {
    'Design': '-dizajn/',
    'Marketing': '-marketing/',
    'Art and culture': '-iskusstvo-i-kultura/',
    'History and archeology': '-istoriya-arheologiya-i-dokumentovedenie/',
    'Quality and control in technical systems': '-kachestvo-i-upravlenie-v-tehnicheskih-sistemah/',
    'Logistics': '-logistika/',
    'Math and information science': '-matematika-informacionnye-nauki-i-tehnologii/',
    'Mechanical engineering and robotics': '-mashinostroenie-avtomatizaciya-i-robototehnika/',
    'The medicine': '-medicina-i-zdravoohranenie/',
    'Chemical and biological sciences': '-himiko-biologicheskie-nauki-i-tehnologii/'  
}


CITIES_RUS = {
    'Москва': 'MSK',
    'Санкт-Питербург': 'SPB',
    'Краснодар': 'KRASNODAR',
    'Казань': 'KAZAN',
    'Екатеринбург': 'EKATERINBURG',
    'Ростов на Дону': 'ROSTOV',
    'Самара': 'SAMARA',
    'Новосибирск': 'NSK',
    'Воронеж': 'VORONEZH',
    'Красноярск': 'KRASNOYARSK'
}
CITIES_ENG = {
    'Moscow': 'MSK',
    'Saint-Petersburg': 'SPB',
    'Krasnodar': 'KRASNODAR',
    'Kazan': 'KAZAN',
    'Ekaterinburg': 'EKATERINBURG',
    'Rostov na Donu': 'ROSTOV',
    'Samara': 'SAMARA',
    'Novosibirsk': 'NSK',
    'Voronezh': 'VORONEZH',
    'Krasnoyarsk': 'KRASNOYARSK'
}

# only parser -------------------------------------------------------------------------
headers = {
    'User-Agent': random_user_agent
}

non_sub = True
user_city = ''
user_format = ''
user_program = ''
user_file = ''
user_language = ''



