# OTUS_hw_module2

Программа-поисковик: 
- спрашивает тему для поиска, 
- выясняет количество ссылок для вывода на экран, поисковую систему
- выдает в консоль все ссылки на тему
main.py и function.py - сделано через парсинг результата гетзапроса
main2.py и function2.py - сделано через парсинг html файла страницы, которая сохраняется при запросе к ней.

В задании использованы библиотеки requests и beautifulsoap.
Про рекурсивный поиск я не особо понял, что именно нужно делать.
Если имелось в виду, что нужно пройтись по ссылкам, которые выдаются поисковой системой и в этих сайтах найти все ссылки,
то можно добавить функцию (например, def rec_search(url)) по поиску всех a href тегов на этих страницах.
Прописать поиск по списку из ссылок поисковика через цикл for и в каждой выполнить rec_search(url), 
вот только в таком случае выдача в консоль будет не самая красивая, т.к. ссылок будет великое множество.


Основная программа - search.py
При запуске запрашивает
