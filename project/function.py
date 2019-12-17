import requests
from bs4 import BeautifulSoup

# функция для поиска по яндексу
def show_result_ya(url, num):
    # поисковый запрос
    r = requests.get(url)
    res = r.text
    soup = BeautifulSoup(res, 'html.parser')
    list = []
    for element in soup.find("ul", {"class": "serp-list serp-list_left_yes"}).find_all('a', {
        "class": 'link link_theme_outer path__item i-bem'}):
        y = "Результат: {0}\n{1}".format(element.text, element.get('href'))
        # сохранение результатов в список для дальнешейго пользования
        list.append(y)

    for i in range(0, int(num)):
        print(list[i])

# функция для поиска по гуглу
def show_result_go(url, num):
    r = requests.get(url)
    res = r.text
    soup = BeautifulSoup(res, 'html.parser')
    list = []
    for element in soup.find_all("div", {"class": "ZINbbc xpd O9g5cc uUPGi"}):

        link = "Результат: {0}".format(element.text)
        list.append(link)
    for i in range(0, int(num)):
        print(list[i])


