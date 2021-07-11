__author__ = 'Дмитрий Назаркин'

# Добавить возможность редактирования данных при помощи отдельного скрипта: передаём ему номер записи и новое значение.
# При этом файл не должен читаться целиком — обязательное требование. Предусмотреть ситуацию, когда пользователь вводит
# номер записи, которой не существует.

import sys, os

# проверки
if not sys.argv[1:] or len(sys.argv[1:]) != 2 or not sys.argv[1].isdigit():
    print('Нужно указать номер строки с записью и новое значение (прим. 3 44,5)')
    exit(0)

position = int(sys.argv[1])
new_data = sys.argv[2]
flag_found = None

# читаем файл, ищем и зазу же пишем tmp файл
with open('bakery.csv', encoding='utf-8') as f:
    with open('bakery_tmp.csv', 'w', encoding='utf-8') as f_tmp:
        curr_line = 1
        for line in f:
            if curr_line == position:
                f_tmp.write(f'{new_data}\n')
                flag_found = 1
            else:
                f_tmp.write(line)
            curr_line += 1

# если не нашли что менять, то удаляем временный файл
if not flag_found:
    os.remove('bakery_tmp.csv')
    print('Позиция не найдена в файле')
else:
    # делаем временный файл постоянным
    os.rename('bakery_tmp.csv', 'bakery.csv')
    print('Данные успешно заменены')
