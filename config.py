from fake_useragent import UserAgent
ua = UserAgent()
random_user_agent = ua.random



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


headers = {

    'User-Agent': random_user_agent
}

# (mb need)
#cookies = {
#    'cookie': '_ym_uid=1660495465903107549; _ym_d=1660495465; _ga=GA1.2.2014700797.1660495465; popup-asterisk=1; popup-setup=1; popup-pack=1; stories_show=5; banner_reg=R1; user_reg=2291015%7E96605EA5943B0763; __lhash_=1a45fb87cf78756c2819ba0e79774dc3; _gid=GA1.2.821530593.1667579530; _gat=1; rmass=14%2C115%2C123%2C145; r_fresh_32=1; _ym_isad=1; _ym_visorc=w; current-page=001; city_id=1; __js_p_=538,1800,0,0,0; __jhash_=2; __jua_=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20WOW64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F107.0.0.0%20Safari%2F537.36; __hash_=5a955ec0e992cb1f25a177d8c909e89b'
#}

user_city = ''
user_format = ''

#tg_bot
TOKEN = ''

first_message_from_bot = f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\nYou have launched the university parser.\nPlease select the city by which universities will be searched.\nThe result will be send you in 'json'"
