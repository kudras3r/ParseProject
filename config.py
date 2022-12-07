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
              
first_message_from_bot = f"➖\nYou have launched the university parser.\nPlease press  <b>'Go parse 👁‍🗨'</b> and select the city by which universities will be searched.\n➖\nThe result will be send you in <b>'json' or 'xlsx'</b> file"

# for parser an bot -------------------------------------------------------------------
PROGRAMS = {
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

CITIES = {
    'Moscow': 'MSK',
    'Saint Petersburg': 'SPB',
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

user_city = ''
user_format = ''
user_program = ''
user_file = ''



