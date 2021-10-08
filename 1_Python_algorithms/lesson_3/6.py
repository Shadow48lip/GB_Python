# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint

arr = [randint(1, 100) for i in range(50)]
print(arr)

sorted_keys = sorted(arr)
# print('min', sorted_keys[0], 'max', sorted_keys[len(arr)-1])

index_min = arr.index(sorted_keys[0])
index_max = arr.index(sorted_keys[len(arr)-1])
# print(index_min, index_max)

if index_min < index_max:
    arr_cut = arr[index_min+1:index_max]
else:
    arr_cut = arr[index_max+1:index_min]

print('Список сложения',arr_cut)
print('сумма', sum(arr_cut))