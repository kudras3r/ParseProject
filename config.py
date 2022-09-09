URL = 'postupi.online/programmy-obucheniya/bakalavr/razdel-matematika-informacionnye-nauki-i-tehnologii/?utm_source=postupi.online&utm_medium=referral&utm_campaign=postupi.online&utm_referrer=postupi.online'

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
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://postupi.online/programmy-obucheniya/bakalavr/razdel-matematika-informacionnye-nauki-i-tehnologii/',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

cookies = {
    'cookie': '_ym_uid=1660495465903107549; _ym_d=1660495465; _ga=GA1.2.2014700797.1660495465; popup-asterisk=1; user_reg=2291015%7E96605EA5943B0763; popup-setup=1; popup-pack=1; __lhash_=b147fee286332650df088a9787c9d6e2; banner_val=H764%2CH787%2CH784%2CH797%2CH647%2CH785; stories_show=5; _gid=GA1.2.1020852239.1661339864; rmass=14%2C115%2C123%2C142%2C145; r_fresh_32=1; _ym_isad=1; current-page=001; city_id=1; __js_p_=879,1800,0,0,0; __jhash_=1109; __jua_=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20WOW64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F104.0.0.0%20Safari%2F537.36; __hash_=6edc2419e16dd4d9c57f789b5077a8e1'
}

user_city = ''

TOKEN = ''

first_message_from_bot = f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\nYou have launched the university parser.\nPlease select the city by which universities will be searched.\nThe result will be send you in 'json'"
