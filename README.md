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
