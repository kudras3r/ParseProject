URL = 'https://postupi.online/programmy-obucheniya/bakalavr/razdel-matematika-informacionnye-nauki-i-tehnologii/'

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

# Header an cookie for requests
headers = {
    'User-Agent': {your user-agent}
}

cookies = {
    'cookie': {your cookies}
}

user_city = ''

TOKEN = ''

first_message_from_bot = f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\nYou have launched the university parser.\nPlease select the city by which universities will be searched.\nThe result will be send you in 'json'"
