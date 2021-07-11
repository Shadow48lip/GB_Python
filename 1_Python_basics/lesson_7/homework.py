"""
Task1
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp


Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена
папок под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить
данные о вложенных папках и файлах (добавлять детали)?
"""
import os

pattern = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}  # we can save .json
for root, folders in pattern.items():
    if os.path.exists(root):
        print(root, 'существует')
    else:
        for folder in folders:
            cur_dir = os.path.join(root, folder)
            if os.path.exists(cur_dir):
                print(cur_dir, 'существует')
            else:
                os.makedirs(cur_dir)

"""
Task2
*(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со 
следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html


Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом 
текстовом редакторе «руками» (не программно); предусмотреть возможные исключительные 
ситуации, библиотеки использовать нельзя.
"""
# pip install pyyaml

import yaml
import os

d = {'my_project':
    [{'settings': [
        '__init__.py', 'dev.py', 'prod.py'
    ],
    },
        {'mainapp': [
            '__init__.py', 'models.py', 'views.py', {'templates': [{
                'mainapp': ['base.html', 'index.html']}]
            }]},
        {'authapp': ['__init__.py', 'models.py', 'views.py', {'templates': [{
            'authapp': ['base.html', 'index.html']}]
        }
                     ]
         }
    ]
}
f = open('config.yaml', 'w')
f.write(yaml.dump(d))
f.close()

with open("config.yaml") as y_file:
    d = yaml.safe_load(y_file)


def create_data(data):
    for folder, data_tmps in data.items():
        if not os.path.exists(folder):
            os.mkdir(folder)
        os.chdir(folder)
        for data_tmp in data_tmps:
            if isinstance(data_tmp, dict):
                create_data(data_tmp)
            else:
                if not os.path.exists(data_tmp):
                    if '.' in data_tmp:
                        with open(data_tmp, 'w') as f:
                            f.write('')
    else:
        os.chdir('../')


create_data(d)

"""
Task3
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или 
«руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку 
templates, например:
|--my_project
   ...
   |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
"""
import os
import shutil
my_dir = 'task3'
if not os.path.exists(my_dir):
    os.mkdir(my_dir)

folder = r'my_project'
files = []


for r, d, f in os.walk(folder):
    for file in f:
        if '.html' in file:
            files.append(os.path.join(r, file))
for path in files:
    folder = os.path.join(my_dir, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder):
        os.mkdir(folder)
    save_path = os.path.join(folder, os.path.basename(path))
    shutil.copy(path, save_path)

"""
Task4
Написать скрипт, который выводит статистику для заданной папки в виде словаря, 
в котором ключи — верхняя граница размера файла (пусть будет кратна 10), 
а значения — общее количество файлов (в том числе и в подпапках), размер которых 
не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }

Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""
import os
files = []
for r, d, f in os.walk('./'):
    for file in f:
        file_path = os.path.join(r, file)
        files.append(os.stat(file_path).st_size)
max_size = max(files)

i = 1
out_dict = {}

for _ in range(len(str(max_size))):
    i *= 10
    out_dict[i] = 0

for file in files:
        out_dict[10 ** len(str(file))] += 1


print(out_dict)


"""
Task5
*(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде 
словаря, в котором ключи те же, а значения — кортежи вида 
(<files_quantity>, [<files_extensions_list>]), например:
    {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }

Сохраните результаты в файл <folder_name>_summary.json в той же папке, 
где запустили скрипт.
"""

import os
import json

files = []
for r, d, f in os.walk('./'):
    for file in f:
        file_path = os.path.join(r, file)
        files.append((file_path.split('.')[-1], os.stat(file_path).st_size))
max_size = max(files, key=lambda x: x[1])[1]

i = 1
out_dict = {}

for _ in range(len(str(max_size))):
    i *= 10
    out_dict[i] = (0, [])

for file in files:
    num, ext_list = out_dict[10 ** len(str(file[1]))]
    ext_list.append(file[0])
    ext_list = list(set(ext_list))
    out_dict[10 ** len(str(file[1]))] = (num + 1, ext_list)

print(out_dict)

with open(os.path.basename(os.getcwd()) + '_summary.json', 'w') as f_json:
    json.dump(out_dict, f_json)
