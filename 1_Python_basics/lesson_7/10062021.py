# Методичка: https://docs.google.com/document/d/1KWM6ZG4zhYa1xA3IohZh7rg0A_wFqeU0bxNwbyEcYsQ/edit#
# В модуле os.path есть ещё много полезных функций для работы с файловой системой:
# abspath() — возвращает абсолютный путь;
# basename() — возвращает имя файла из абсолютного или относительного пути;
# dirname() — возвращает имя (путь) папки, в которой расположен файл;
# split() — делит путь к файлу на путь к папке и имя файла (заменяет вызов двух предыдущих функций);
# relpath() — определяет путь к файлу относительно другой папки, не обращается к реальной файловой системе, чисто вычисления (полезна при сохранении путей к файлам в базе данных относительно заданного корня);
# join() — склеивает путь из частей (надеемся, вы не делаете это через строки!);
# exists() — проверяет существование объекта файловой системы.

# Что ещё полезного есть в модуле shutil? Функции для копирования файлов:
# copyfileobj() —  копирование одного файлового объекта в другой;
# copyfile() — копирование содержимого одного файла в другой (настройки доступа не копируются);
# copy() — копирование файла (копируются настройки доступа);
# copy2() -— копирование файла (копируются настройки доступа и метаданные — о них подробнее позже).


# import os
# folder = r'../venv/bin'
# py_files = [x for x in os.listdir(folder) if x.lower().endswith('.py')]
# # print(py_files)
# print([os.path.join(folder, x) for x in py_files])

# import os
# from time import perf_counter
#
# folder = r'C:\Users\ivan_\Desktop\pyhton_11_lessons\11_les7\some_data'
# size_thr = 15 * 2 ** 10 #(15 * 1024)
# start = perf_counter()
# small_files = [item for item in os.listdir(folder)
#                if os.stat(os.path.join(folder, item)).st_size < size_thr]
# print(len(small_files), perf_counter() - start)
#
# start = perf_counter()
# small_files_2 = [item.name for item in os.scandir(folder) if item.stat().st_size < size_thr]
# print(len(small_files_2), perf_counter() - start)

# import os

# print(os.path.abspath('321'))
# folder = r'C:\Users\ivan_\Desktop\pyhton_11_lessons\11_les7\nginx_log.txt'
# folder = r'C:\Users\ivan_\Desktop'
# print(os.path.basename(folder))
# print(os.path.dirname(folder))
# print(os.path.split(folder))
# print(os.path.relpath('nginx_log.txt', start=folder))
# print(os.path.exists('qwe'))
# os.mkdir()
# os.makedirs('2\\2')
# os.rename('2', 'folder_2')
# os.rename('folder_2\\2', './2')
# os.remove('qwe')
# import os
# os.rmdir('folder_2')

import shutil

# shutil.rmtree('folder_2')

# shutil.copyfile('users.csv', r'1\users.csv')
# shutil.copy('321', '1')
# shutil.copy2('users.csv', r'1\users.csv')

# shutil.copyfileobj(a, b)

# 7
# for path in os.listdir('321'):
#     print(path)

# for root, dir, files in os.walk('321'):
#     print(root, dir, files)


# Встроенные классы исключений иерархия https://docs.python.org/3.8/library/exceptions.html#exception-hierarchy
# Помимо уже встретившихся нам исключений (ValueError, ZeroDivisionError, FileExistsError, FileNotFoundError),
# достаточно часто в коде бывают полезны:
# AttributeError — попытка обратиться к несуществующему атрибуту или методу;
# IndexError — ошибка индекса (в списке), обращение к элементу с индексом за пределами существующих;
# KeyError — ошибка ключа (в словаре), обращение к элементу словаря, которого в нём нет;
# TypeError — попытка передать функции аргумент не того типа (например, преобразовать список в число float([1,])) или
# выполнить операцию над операндом не того типа


# import os
# print(os.getcwd())
# os.chdir('1')
# print(os.getcwd())
# os.mkdir('123213')
# try:
#     print(1/int(input()))
# except ZeroDivisionError:
#     print('Деление на ноль')
# except ValueError:
# #     print('введено не число!')
#
#
# try:
#     with open('qwe.csv') as f:
#         print(int(f.read()))
# except FileNotFoundError:
#     print('файл не найден')
# except Exception as e:
#     print('global error', e)

# try:
#     with open('qwe.csv') as f:
#         print(int(f.read()))
# except Exception as e:
#     print('global error', e)
# except FileNotFoundError:
#     print('файл не найден')

# try:
#     f = open('qwe.txt')
#     print(int(f.read()))
# except FileNotFoundError:
#     print('файл не найден')
# except ValueError:
#     print('not int')
# else:
#     print('все ок')
# finally:
#     f.close()
#
# print(f.closed)

# i = 0
# try:
#     raise ZeroDivisionError
# except ZeroDivisionError:
#     print('0')


# def char_in_str(txt)

# raise ValueError


# class CalcError(Exception):
#     pass
#
# raise CalcError

