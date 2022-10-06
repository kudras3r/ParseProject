

# Imports
import requests
import openpyxl
import json
import sys
from bs4 import BeautifulSoup
from colorama import Style, Fore, Back
from config import *
from openpyxl.styles import Alignment
from openpyxl.styles import Font


# Function for choosing user city 
def select_city() -> str:
    
    global user_city

    print(Fore.RED + "You have launched the university parser.\nPlease select the city by which universities will be searched.\nThe result will be send you in 'json' or 'xlsx'" + Style.RESET_ALL)
    print('-'*120)
    print('Choose city. Enter the short name.')
    
    for name, short_name in CITIES.items():
        print(Fore.WHITE + f'for {name} enter: {Fore.CYAN + short_name + Style.RESET_ALL}')

    user_city = input('>>> ')
        
    if user_city.upper() in CITIES.values():

        user_URL = f'https://{user_city.lower()}.postupi.online/programmy-obucheniya/bakalavr/razdel-matematika-informacionnye-nauki-i-tehnologii/'

    else:
        print('Invalid city code! Try again.')
        select_city()
        
    
    return user_URL



# Creating xlsx file
def xlsx_data(data: dict, city=user_city):
    
    row1 = 2

    book = openpyxl.Workbook()
    sheet = book.active

    sheet['A1'] = 'Направление'
    sheet['B1'] = 'Университеты'
    sheet['C1'] = 'Баллы'
    
    sheet['A1'].font = Font(name='Arial Cyr', charset=204, family=2.0, b=True, color='0070C0', size=14)
    sheet['B1'].font = Font(name='Arial Cyr', charset=204, family=2.0, b=True, color='0070C0', size=14)
    sheet['C1'].font = Font(name='Arial Cyr', charset=204, family=2.0, b=True, color='0070C0', size=12)
    
    sheet.column_dimensions['A'].width = 70
    sheet.column_dimensions['B'].width = 70

    for programm in data.keys():
        univ_info = ''
        sheet.cell(row=row1, column= 1).value = programm
        for univ_name, link in data[programm].items():
            if univ_name != 'Баллы на бюджет: ':
                univ_info += f' \n{univ_name}: {link}'
            else:
                sheet[f'B{row1}'].alignment = Alignment(wrapText=True)
                sheet.cell(row=row1, column=3).value = link


        sheet[f'A{row1}'].font = Font(name='Arial Cyr', charset=204, family=2.0, b=True, color='9a76f5', size=13)
        sheet[f'B{row1}'].font = Font(name='Arials', charset=204, family=2.0, b=True, color='4f1818', size=12)
        
        sheet.cell(row=row1, column=2).value = univ_info.replace(',', '')

        row1 += 1
    
    
            

    book.save(f"{city}_result.xlsx")
    book.close()


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
            
            url = f'{URL}?page_num={page}'
            
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

    data = get_data(select_city())
    xlsx_data(data, user_city)
    #main()
