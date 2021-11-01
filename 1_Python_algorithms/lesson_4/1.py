# Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.

# ЗАДАЧА
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

n = 20
ind_min = 0
dig_min = 101
ind_max = 0
dig_max = 0

a = [randint(1, 100) for i in range(n)]
print('исходный случайный список:', a)

# Вариант нормальный
for i in range(n):
    if a[i] < dig_min:
        ind_min, dig_min = i, a[i]
    if a[i] > dig_max:
        ind_max, dig_max = i, a[i]

a[ind_min], a[ind_max] = a[ind_max], a[ind_min]
print('измененный список:', a)

"""
Предположительно сложность алгоритма O(n), так как мы пробегаем весь список полностью и чем он длиннее, тем дольше
будет работать. Операция замены значений не должна быть тяжелой, так как мы не меняем размер списка.
Накладных расходовало по памяти так же не будет, пространственная сложность  O(1), так как обошлись 
без доп списков, а используем лишь несколько маленьких переменных.

Решить как-то принципиально иначе и быстрее не вижу вариантов. Городить тут циклы в цикле не оправдано, получим
O(n**2) или O(n**3)
"""
