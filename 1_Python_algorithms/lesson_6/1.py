# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Python 3.9, MacOS 64-bit

import sys

# Задача 1
year = int(input('Введите год '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'{year} год високосный')
else:
    print(f'{year} год НЕ високосный')

print(sys.getsizeof(year))
''' 28 байт занимает четырехначное число. int положительное '''


# Задача 2

digits = [x for x in range(2, 100)]
dividers = {x: 0 for x in range(2, 10)}

for i in digits:
    for d, count in dividers.items():
        if i % d == 0:
            dividers[d] += 1
print(dividers)

print(sys.getsizeof([])) # 56, хоят по методичке 40
print(len(digits), type(digits), sys.getsizeof(digits))
print(len(dividers), type(dividers), sys.getsizeof(dividers))
'''
Список digits занимает 920 байт и, судя по эксперементам, память выделяется порциями с запасом.
Так, если увеличить список до 109 ячеек, то память расширяется до 1080 байт сразу.
Расчетное потребление по списку 56 + 8*98 = 840 - это ссылки на элементы в памяти.
Фактически интерпритатор скушал 920 байт.
Плюс 98*28 = 2744 байта на сами данные. Итого 2744 + 920 = 3664 байт.

Можно было бы сэкономить на списке сгенерировав кортэж, он потребляет меньшее памяти 24+8*длина, проив 40+8*длина списка
А еще итерируемый объект расходует еще меньше памяти. Тут бы он подошел даже лучше.

Ну и такая же история со словарем dividers.
16*28 = 448 + 360 = 808 байт на словарь.

Временные переменные i, d, count содержат в себе которкие числа по 28 байт.
'''

# Задача 3

from random import randint

arr = [randint(1, 100) for i in range(50)]
print(arr)

sorted_keys = sorted(arr)
index_min = arr.index(sorted_keys[0])
index_max = arr.index(sorted_keys[len(arr)-1])

if index_min < index_max:
    arr_cut = arr[index_min+1:index_max]
else:
    arr_cut = arr[index_max+1:index_min]

print('Список сложения',arr_cut)
print('сумма', sum(arr_cut))

print(len(arr), type(arr), sys.getsizeof(arr))
print(len(arr_cut), type(arr_cut), sys.getsizeof(arr_cut))
print(sys.getsizeof(index_min), sys.getsizeof(index_max))

'''
Список arr с фиксированной длиной в 50 ячеек, состоящий из целых чисел 50*28 = 1400 + 472 = 1872
Список arr_cut с рандомной длиной (сейчас 3) 56 + 8*3 = 80 + 3*28 = 164
И плюс 2 переменные по 28 байт = 56
Всего 56 + 164 + 1872 = 2092
'''