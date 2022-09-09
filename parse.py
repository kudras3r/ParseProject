

# Imports
from bs4 import BeautifulSoup
import requests
import json
import sys
from colorama import Style, Fore, Back
from config import *


# Function for choosing user city 
def select_city() -> str:
    
    global user_city

    print(Fore.RED + "You have launched the university parser.\nPlease select the city by which universities will be searched.\nThe result will be saved to a folder called '()_result.json'" + Style.RESET_ALL)
    print('-'*120)
    print('Choose city. Enter the short name.')
    
    for name, short_name in CITIES.items():
        print(Fore.WHITE + f'for {name} enter: {Fore.CYAN + short_name + Style.RESET_ALL}')

    user_city = input('>>> ')
        
    if user_city.upper() in CITIES.values():

        user_URL = f'https://{user_city.lower()}.postupi.online/programmy-obucheniya/bakalavr/razdel-matematika-informacionnye-nauki-i-tehnologii/?utm_source=postupi.online&utm_medium=referral&utm_campaign=postupi.online&utm_referrer=postupi.online'

    else:
        print('Invalid city code! Try again.')
        select_city()
        
    
    return user_URL


# Data collection function(url) -> data
def get_data(URL) -> dict:

    result_dict = dict()

    ''' Make request to 1st page '''
    s = requests.Session()
    response = s.get(URL, headers=headers, cookies=cookies)
    
    ''' Check status code '''
    if response.status_code == 200:
        
        print(f'status code: {response.status_code}')
        
        ''' Create a soup for parse '''
        soup = BeautifulSoup(response.text, 'lxml')
        navigation_count = int(soup.find('div', class_='invite fetcher').find_all('a', class_='paginator')[-1].text)
    
        ''' Iterate all pages '''
        for page in range(1, navigation_count + 1): 
        
            print(f'Processing page {page}/{navigation_count}')
            
            url = f'{URL}&page_num={page}'
            
            response = s.get(url, headers=headers, cookies=cookies)
            soup = BeautifulSoup(response.text, 'lxml')
        
            all_programs_on_page = soup.find('ul', class_='list-unstyled list-wrap').find_all('div', class_='list__info')
            
            ''' Iterate all program on pages'''
            for program in all_programs_on_page:

                program_url = program.find('h2', class_='list__h').find('a')['href']
                program_name = program.find('h2', class_='list__h').find('a').text
                
                if program.find('span', class_='list__score-sm') != None:
                    
                    min_points = program.find('span', class_='list__score-sm').find('b').text
                    
                else:
                    min_points = 'No info'

                if 'vuz' in program_url:
                
                    univ_name = program.find('p', class_='list__pre').find('a').text
                    univ_link = program.find('h2', class_='list__h').find('a')['href']
                
                    result_dict[program_name] = {univ_name: univ_link}
                    result_dict[program_name]['Баллы на бюджет: '] = min_points
                    
                else:
                    univ_names = []
                    univ_links = []

                    response = s.get(program_url, headers=headers, cookies=cookies)
                    soup = BeautifulSoup(response.text, 'lxml')

                    univ_info = soup.find('div', class_='detail-box__item detail-box__item_upcase').find_all('a')

                    for info in univ_info:
                        univ_names.append(info.text.replace(u"\u00A0", ""))
                        univ_links.append(info['href'])

                    result_dict[program_name] = dict(zip(univ_names, univ_links))
                    result_dict[program_name]['Баллы на бюджет: '] = min_points
        
        print('-'*120)

        return result_dict
    
    else:
        print('Error')
        sys.exit

# Function for testing (not working at main code)
def print_result(result: dict):

    for program, univ_list in result.items():
        
        print(Fore.BLUE + '-'*((120-len(program))//2) + Fore.BLUE + program + '-'*((120-len(program))//2))

        for name, link in univ_list.items():

            print(f'{Fore.WHITE + name}: {Fore.CYAN + link}')


# Main function
def main():
    
    url = select_city()

    data = get_data(url)
    
    ''' Creating json with data'''
    with open(f'{user_city}_result.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)    

    print(Fore.GREEN + f'Succesfuly! Check {user_city}_result.json' + Style.RESET_ALL)


if __name__ == '__main__':
    main()
