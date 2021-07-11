"""Task 1
Выяснить тип результата выражений:
15 * 3
15 / 3
15 // 2
15 ** 2"""
print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 3))
print(type(15 ** 3))

""" Task 2
Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
'была', '+5', 'градусов']

Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом)
и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха',
'была', '"', '+05', '"', 'градусов']

Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов

Подумать, какое условие записать, чтобы выявить числа среди элементов списка? 
Как модифицировать это условие для чисел со знаком?
"""

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
           'была', '+5', 'градусов']

new_list = []
for elem in my_list:
    if elem.isdigit():
        new_list.extend(['"', f'{int(elem):02}', '"'])
    elif (elem.startswith('+') or elem.startswith('-')) and elem[1:].isdigit():
        new_list.extend(['"', f'{elem[0]}{int(elem[1:]):02}', '"'])
    else:
        new_list.append(elem)

out_info = ' '.join(new_list)
print(out_info)

# to perfect out (delete whitespaces):
# find indexes with " symbol
symbol_idxs = []
for idx, letter in enumerate(out_info):
    if letter == '"':
        symbol_idxs.append(idx)

# some logic to find delete indexes
for idx in range(len(symbol_idxs)):
    if idx % 2 == 0:
        symbol_idxs[idx] = symbol_idxs[idx] + 1
    else:
        symbol_idxs[idx] = symbol_idxs[idx] - 1

# delete indexes from original string
for del_idx in reversed(symbol_idxs):
    out_info = out_info[:del_idx] + out_info[del_idx+1:]

"""Task 3
*(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). 
Эта задача намного серьёзнее, чем может сначала показаться."""

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
           'была', '+5', 'градусов']

idx = 0
while idx < len(my_list):
    if my_list[idx].isdigit():
        my_list.insert(idx, '"')
        my_list[idx + 1] = f'{int(my_list[idx + 1]):02}'
        my_list.insert(idx + 2, '"')
        idx += 2

    elif (my_list[idx].startswith('+') or my_list[idx].startswith('-')) and \
            my_list[idx][1:].isdigit():

        my_list.insert(idx, '"')
        my_list[idx + 1] = f'{my_list[idx + 1][0]}{int(my_list[idx + 1][1:]):02}'
        my_list.insert(idx + 2, '"')
        idx += 2
    idx += 1

out_info = ' '.join(my_list)  # to perfect out go to task 2
print(out_info)
"""Task 4
Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 
'токарь высшего разряда нИКОЛАй', 'директор аэлита']

Известно, что имя сотрудника всегда в конце строки. Сформировать из этих 
имён и вывести на экран фразы вида: 'Привет, Игорь!' Подумать, как получить 
имена сотрудников из элементов списка, как привести их к корректному виду. 
Можно ли при этом не создавать новый список?
"""
bad_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
            'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for position in bad_list:
    print('Привет', position.split()[-1].title())

"""Task 5
Создать вручную список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]

Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в 
виде <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить 
рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек 
(должно быть 07 коп или 00 коп).  

Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, 
что объект списка после сортировки остался тот же).

Создать новый список, содержащий те же цены, но отсортированные по убыванию.
Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров 
по возрастанию, написав минимум кода?
"""

goods = [57.8, 46.51, 97, 10, 20.14, 30.18, 40.05, 50.98, 9077, 1]
for good in goods:
    rub = int(good)
    kk = (good - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп')  # 02 - добавить поле нулей 2шт,  .0f - округление 0 знаков после запятой



goods = [57.8, 46.51, 97, 10, 20.14, 30.18, 40.5, 50.98, 9077, 1]
print(id(goods))
goods.sort()
print(id(goods))
for good in goods:
    rub = int(good)
    kk = (good - int(good)) * 100
    print(f'{rub} руб {kk:02.0f} коп')  # 02 - добавить поле нулей 2шт,  .0f - округление 0 знаков после запятой


goods = [57.8, 46.51, 97, 10, 20.14, 30.18, 40.5, 50.98, 9077, 1, 23.7]
for good in sorted(goods)[::-1][:5]:
    rub = int(good)
    kk = (good - int(good)) * 100
    print(f'{rub} руб {kk:02.0f} коп')  # 02 - добавить поле нулей 2шт,  .0f - округление 0 знаков после запятой

# one line
print([f'{int(good)} руб {(good - int(good)) * 100:02.0f} коп' for good in sorted(goods)[::-1][:5]])