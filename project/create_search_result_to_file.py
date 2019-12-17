import requests
from bs4 import BeautifulSoup

def search_func(url):
    r = requests.get(url)
    res = r.text
    my_file = open("search_result_webpage.html", "w", encoding="utf-8")
    my_file.write(res)
    my_file.close()


def show_result_ya(num):

    html = open('search_result_webpage.html', encoding="utf-8").read()
    soup = BeautifulSoup(html, 'html.parser')
    list = []
    for element in soup.find("ul", {"class": "serp-list serp-list_left_yes"}).find_all('a', {"class": 'link link_theme_outer path__item i-bem'}):
        y = "Результат: {0}\n{1}".format(element.text, element.get('href'))

        list.append(y)

    for i in range(0, int(num)):
        print(list[i])

def show_result_go(num):
    html = open('search_result_webpage.html', encoding="utf-8").read()
    soup = BeautifulSoup(html, 'html.parser')
    list = []
    for element in soup.find_all("div", {"class": "ZINbbc xpd O9g5cc uUPGi"}):
        x = "Результат: {0}".format(element.text)

        list.append(x)

    for i in range(0, int(num)):
        print(list[i])





