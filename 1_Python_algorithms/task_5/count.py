
# Посчитать количество уникальных элементов в последовательности

# 1 способ
'''
from collections import Counter


cnt = Counter(input().split(' '))

print(len(cnt))
'''
# 2 способ

put = input().split(' ')

d_dict = {}

for i in put:
    if i not in d_dict:
        d_dict[i] = 1
    else:
        d_dict[i] += 1

print(len(d_dict))
