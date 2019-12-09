#main2.py и function2.py - сделано через парсинг результата гетзапроса, который сохраняется в файл
import function2


def websearch():

    search = input('Что вы хотите найти? ')
    search_engine = input('Выберите поисковую систему: Яндекс или Google ')
    search_numdoc = input('Введите количество ссылок(10, 20, 30, 50, 100): ')

    ya = 'https://yandex.ru/search/?text=' + search + '&' + 'numdoc=' + search_numdoc
    goo = 'https://www.google.ru/search?q=' + search + '&' + 'num=' + search_numdoc

    if search_engine.lower() in ('яндекс', 'yandex'):
        function2.search_func(ya)
        function2.show_result_ya(search_numdoc)

    elif search_engine.lower() in ('гугл', 'google'):
        function2.search_func(goo)
        function2.show_result_go(search_numdoc)
    else:
        print('Не верно задана поисковая система')
websearch()