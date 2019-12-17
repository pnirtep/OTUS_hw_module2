# OTUS_hw_module2

Программа-поисковик: 
- спрашивает тему для поиска, 
- выясняет количество ссылок для вывода на экран, поисковую систему
- выдает в консоль все ссылки на тему
search.py и create_search_result.py - сделано через парсинг результата гетзапроса
search_to_file.py и create_search_result_to_file.py - сделано через парсинг создаваемого html-файла страницы, которая сохраняется при запросе к ней.

В задании использованы библиотеки requests и beautifulsoap.
Про рекурсивный поиск я не особо понял, что именно нужно делать.
Если имелось в виду, что нужно пройтись по ссылкам, которые выдаются поисковой системой и в этих сайтах найти все ссылки,
то можно добавить функцию (например, def rec_search(url)) по поиску всех a href тегов на этих страницах.
Прописать поиск по списку из ссылок поисковика через цикл for и в каждой выполнить rec_search(url), 
вот только в таком случае выдача в консоль будет не самая красивая, т.к. ссылок будет великое множество.


Основная программа - search.py

```python
//python code
    search = input('Что вы хотите найти? ')
    search_numdoc = input('Введите количество ссылок(10, 20, 30, 50, 100): ')
    search_engine = input('Выберите поисковую систему: Яндекс или Google ')
    
    # ссылки для поисковых запросов
    ya = 'https://yandex.ru/search/?text=' + search + '&' + 'numdoc=' + search_numdoc
    goo = 'https://www.google.ru/search?q=' + search + '&' + 'num=' + search_numdoc
```
Далее происходит проверка на то, в какой системе осуществлять поиск и в каком количестве выводить результаты

```python
//python code
    if search_engine.lower() in ('яндекс', 'yandex', 'ya'):
        create_search_result.show_result_ya(ya, search_numdoc)

    elif search_engine.lower() in ('гугл', 'google'):
        create_search_result.show_result_go(goo, search_numdoc)
    else:
        err = input('Не верно задана поисковая система, начать заново? Y/N ')
        if err.lower() in ('y', 'yes', 'д', 'да'):
            websearch()
        else:
            print('Удачи в поисках!')
            exit()
```

Данные о поисковой ситеме, запросе и количестве уходят в соответствующие функции:
Для обработки данных с яндекса

```python
//python code
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
```

Для обработки данных с гугла

```python
//python code
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
```

