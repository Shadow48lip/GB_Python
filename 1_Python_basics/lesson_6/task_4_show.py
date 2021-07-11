__author__ = 'Дмитрий Назаркин'

# Для чтения данных реализовать в командной строке следующую логику:
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму
# числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1.

import sys

file_db = 'bakery.csv'

# просто запуск скрипта - вывод всех записей
if not sys.argv[1:]:
    print('Вывод всех записей:')
    with open(file_db, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
elif len(sys.argv[1:]) == 1:
    if sys.argv[1].isdigit():
        start = int(sys.argv[1])
    else:
        start = 1

    print(f'Вывод всех записей начиная с {start} и до конца:')
    with open(file_db, encoding='utf-8') as f:
        curr_line = 1
        for line in f:
            if curr_line >= start:
                print(line, end='')
            curr_line += 1

elif len(sys.argv[1:]) == 2:
    if sys.argv[1].isdigit() and sys.argv[2].isdigit():
        start = int(sys.argv[1])
        stop = int(sys.argv[2])
    else:
        print('Укажите правильные интервалы начала и конца выборки (прим. 2 5)')
        exit(1)

    print(f'Вывод всех записей начиная с {start} и до {stop}')
    with open(file_db, encoding='utf-8') as f:
        curr_line = 1
        for line in f:
            if curr_line >= start and curr_line <= stop:
                print(line, end='')
            curr_line += 1
            # не нужно добегать до конца файла, прирываем
            if curr_line > stop:
                break

print('Без параметров - вывод всех записей, одно число - вывод всех строк начиная с указанной, два числа - вывод в диапазоне')