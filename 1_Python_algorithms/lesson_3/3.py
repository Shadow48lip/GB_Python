# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

n = 20
ind_min = 0
dig_min = 101
ind_max = 0
dig_max = 0

a = [randint(1, 100) for i in range(n)]
print('исходный случайный список:', a)

for i in range(n):
    if a[i] < dig_min:
        ind_min, dig_min = i, a[i]
    if a[i] > dig_max:
        ind_max, dig_max = i, a[i]

a[ind_min], a[ind_max] = a[ind_max], a[ind_min]
print('измененный список:', a)
