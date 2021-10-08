# Определить, какое число в массиве встречается чаще всего

from random import randint

# сам список
arr = [randint(1, 10) for i in range(50)]
# словарь со счетчиками на основе списка, set() не нужно и так уникальные значения
stat = dict.fromkeys(arr, 0)

print(arr)

# посчитали
for i in arr:
    stat[i] += 1

print('Statistics:',stat)

# sorted
sorted_keys = sorted(stat, key=stat.get, reverse=True)
print('Чаще всего встречается', sorted_keys[0], '-', stat[sorted_keys[0]],'раз')