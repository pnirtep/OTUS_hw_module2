# main.py и function.py - сделано через парсинг результата гетзапроса
from project import function


def websearch():
    # пользовательский ввод основных параметров поиска
    search = input('Что вы хотите найти? ')
    search_numdoc = input('Введите количество ссылок(10, 20, 30, 50, 100): ')
    search_engine = input('Выберите поисковую систему: Яндекс или Google ')
    # ссылки для поисковых запросов
    ya = 'https://yandex.ru/search/?text=' + search + '&' + 'numdoc=' + search_numdoc
    goo = 'https://www.google.ru/search?q=' + search + '&' + 'num=' + search_numdoc

    # проверка поисковой системы и выполнение функций поиска и вывода
    if search_engine.lower() in ('яндекс', 'yandex', 'ya'):
        function.show_result_ya(ya, search_numdoc)

    elif search_engine.lower() in ('гугл', 'google'):
        function.show_result_go(goo, search_numdoc)
    else:
        err = input('Не верно задана поисковая система, начать заново? Y/N ')
        if err.lower() in ('y', 'yes', 'д', 'да'):
            websearch()
        else:
            print('Удачи в поисках!')
            exit()


websearch()
