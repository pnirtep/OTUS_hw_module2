'''Cделано через парсинг результата гетзапроса, который сохраняется в файл.
Далее из фала собираются нужные url и передаются в консоль
'''
from project import create_search_result_to_file


def websearch():
    # пользовательский ввод основных параметров поиска
    search = input('Что вы хотите найти? ')
    search_engine = input('Выберите поисковую систему: Яндекс или Google ')
    search_numdoc = input('Введите количество ссылок(10, 20, 30, 50, 100): ')

    # ссылки для поисковых запросов
    ya = 'https://yandex.ru/search/?text=' + search + '&' + 'numdoc=' + search_numdoc
    goo = 'https://www.google.ru/search?q=' + search + '&' + 'num=' + search_numdoc

    # проверка поисковой системы и выполнение функций поиска и вывода
    if search_engine.lower() in ('яндекс', 'yandex'):
        create_search_result_to_file.search_func(ya)
        create_search_result_to_file.show_result_ya(search_numdoc)

    elif search_engine.lower() in ('гугл', 'google'):
        create_search_result_to_file.search_func(goo)
        create_search_result_to_file.show_result_go(search_numdoc)
    else:
        print('Не верно задана поисковая система')

websearch()