__author__ = 'Дмитрий Назаркин'

# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби. Известно, что при хранении
# данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая. Написать код,
# загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить
# словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с
# ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать,
# что объём данных в файлах во много раз мзеньше объема ОЗУ.


from itertools import zip_longest
import json

users_dict = {}

f1 = open('users.csv', encoding='utf-8')
f2 = open('hobby.csv', encoding='utf-8')

# Вот так можно было посчитать количество строк через генераторы
# num_lines_users = sum(1 for line in f1)
# num_lines_hobby = sum(1 for line in f2)

for fio, hobby in zip_longest(f1, f2):
    # выходим из скрипта с кодом «1» если в файле с фио меньше записей чем в хобби
    if fio == None:
        f1.close()
        f2.close()
        exit(1)
    else:
        fio = fio.replace(',', ' ').strip()

    if hobby != None:
        hobby = hobby.strip()

    users_dict.update({fio: hobby})

f1.close()
f2.close()

with open("users_hobby.json", "w", encoding='utf-8') as f:
    # Чтоб не ломалась кирилица в json (ensure_ascii=False)
    json.dump(users_dict, f, ensure_ascii=False)

with open("users_hobby.json", encoding='utf-8') as f:
    data = json.load(f)
    print(data)
    print(type(data))

