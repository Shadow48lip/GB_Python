__author__ = 'Дмитрий Назаркин'

# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
# размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), размер
# которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# *(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
# а значения — кортежи вида (<files_quantity>, [<files_extensions_list>])
# {
#     100: (15, ['txt']),
#     1000: (3, ['py', 'txt']),
#     10000: (7, ['html', 'css']),
#     100000: (2, ['png', 'jpg'])
# }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

import os, json

# список целевых папок в генераторе
list_folders = (root for root, _, _ in os.walk('some_data'))

# словари для двух видов выполнения (под зведочкой и без)
stat_dict_a = {}
stat_dict_b = {}

# обходим каталги и наполняем словарь
for folder in list_folders:
    print(folder)
    size = 10

    while True:
        files = [item.name for item in os.scandir(folder)
                 if item.is_file() and item.stat().st_size <= size and item.stat().st_size > size / 10]

        #для задачи без звездочки было бы
        stat_dict_a.setdefault(size, 0)
        stat_dict_a[size] += len(files)

        # для задачи под звездочкой
        extensions = list({file.split('.')[-1] for file in files})
        stat_dict_b.setdefault(size, (0, []))
        old_couner, old_extensions = stat_dict_b[size]
        new_counter = old_couner + len(files)
        new_extensions = set(old_extensions + extensions)
        new_stat = (new_counter, list(new_extensions))
        stat_dict_b[size] = new_stat

        # остановка цикла, если больше файлов не будет
        num_more = sum([1 for item in os.scandir(folder) if item.is_file and item.stat().st_size > size])
        if num_more == 0:
            break

        size *= 10

print(stat_dict_a)
# print(stat_dict_b)

json_file = os.getcwd().split('/')[-1] + '_summary.json'

with open(json_file, 'w') as f:
    json.dump(stat_dict_b, f)

print('Результаты сохранены в файл', json_file)