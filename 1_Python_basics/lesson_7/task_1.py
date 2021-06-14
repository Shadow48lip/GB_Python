__author__ = 'Дмитрий Назаркин'

# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
#
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию
# этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом
# расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
import os
root_path = os.getcwd()

starter_folders = {
    'my_project': ['settings', 'mainapp', 'adminapp', 'authapp'],
    'core': ['cache', 'tmp']
}

path_lists = (os.path.join(root_path, line1, line2) for line1 in starter_folders for line2 in starter_folders[line1])

for folder in path_lists:
    if not os.path.exists(folder):
        os.makedirs(folder)

