import requests
from bs4 import BeautifulSoup
##############################################################
#                                                            #
#                                                            #
# Написать коментарии чтоб все было понятно                  #
# Попробовать соеденить имеющуюся версию с оболочкой         #
# Разобраться с выводом / убрать лишный текст                #
# Прочитать еще раз документацию прекрасного супа            #
# rowspan - кол-во предметов                                 #
# Досмотреть второй урок ютуб / пересмотреть первый еще раз  #
#                                                            #
#                                                            #
###############################################################




URL = 'https://synergy.ru/students/schedule?view_mode=student&param=9455#today'  # ссылка на нужный сайт


def get_html( url, params=None ):   # ф-я которая получает HTML страницы
    r = requests.get( url, params=params)
    return r


def get_content(html):   # мейн ф-я которая ищет нужные эл-ты
    soup = BeautifulSoup(html, 'html.parser')  # обращение к методу прекрасный суп
    items = soup.find_all('tr', class_='today')  # метод файнд в супе
    lesons = []  # задаем пустой список в который поместим нужные данные
    for item in items:  # цикл который ограничевает поиски параметрами items
        lesons.append({
            'date': item.find('span', style=True).get_text(), # выводит дату / см код HTML в формате текста
            'time': item.find('td', title=True).get_text(),  # выводит дату / см время HTML в формате текста
            'leson': item.find('td', title = 'Дисциплина').get_text(), # выводит предмет / см код HTML в формате текста
            'cab': item.find('td', title='№ ауд.').get_text(), # выводит кабинет / см код HTML в формате текста
            #'rowspan': item.find('td', rowspan='3').get_text()
        })
    print (lesons)   # вывод заполненного списка



def parse():   #  проверка статус кода сайта / если все ок == 200
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
parse()
