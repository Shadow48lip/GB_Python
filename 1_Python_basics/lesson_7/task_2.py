__author__ = 'Дмитрий Назаркин'

# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
#
# |--my_project
#    ...
#    |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
#
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая
# решена, например, во фреймворке django.

import os
from shutil import copy


root_path = os.path.join(os.getcwd(), 'templates')

# Ищем файлы
template_files = []
template_files += [(root, file) for root, _dirs, files in os.walk('my_project')
                   for file in files if file.lower().endswith('.html')]

for path, filename in template_files:
    path_to_dir_new = os.path.join('templates', path.split('/')[-1])
    path_to_file_new = os.path.join(path_to_dir_new, filename)
    path_to_file_old = os.path.join(path, filename)
    # print(path_to_dir_new, path_to_file_new)

    # Подготовка каталогов
    if not os.path.exists(path_to_dir_new):
        os.makedirs(path_to_dir_new)

    # Копипрование файлов
    try:
        copy(path_to_file_old, path_to_file_new)
    except OSError as e:
        print('Ошибка с доступа в файловой системе: ', e)
    except Exception as e:
        print('Общая ошибка:', e)
    else:
        print('Файл', filename, 'успешно скопирован')
