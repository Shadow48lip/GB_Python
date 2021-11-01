#4. Написать программу, которая генерирует в указанных пользователем границах:
#* случайное целое число;
#* случайное вещественное число;
#* случайный символ.
#
'''
import random

symbol = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)]

print(random.choice(symbol))

'''

### 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

#print(chr(int(input()+64)))



### 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

#symbol = [chr(i) for i in range(65,91)]

#put1, put2  = input(), input()

#O(n)
def linear_search(symbol, put1, put2=''):
    for i in range(len(symbol)):
        if symbol[i] == put1:
            return i
    '''
    for i in range(len(symbol)):
        if symbol[i] == put1:
            pos1 = i + 1
            break
    for i in range(len(symbol)):
        if symbol[i] == put2:
            pos2 = i + 1
            break

    if pos1 > pos2:
        pos1, pos2 = pos2, pos1

    print(pos1, pos2, pos2-pos1-1)
    '''
#O(log n)

def binary_search(symbol, put, left, right):

    if right <= left:
        return -1
    mid = (left + right) // 2
    if put == symbol[mid]:
        return mid
    
    elif put < symbol[mid]:
        return binary_search(symbol, put, left, mid)
    else:
        return binary_search(symbol, put, mid + 1, right)

#print(symbol)
#print(binary_search(symbol, 'R', 0 , len(symbol))+1)

import time


b = list(range(2999999))

a = time.time()

linear_search(b,2999998)

print(time.time() - a, 'время linear_search' )
# 0.7
a = time.time()

binary_search(b,2999998, 0, len(b))

print(time.time() - a, 'время binary_search' )
# 0.00006

#Пример рекурсии
#_______
def build_mat(size, n):
    if n >= 1:
        print('Создаем низ матрешки', size)
        build_mat(size-1, n-1)
        print('Создаем вверх матрешки', size)
    else:
        return


#build_mat(4,3)


#fact


def fact(n):
    if n == 1 or n == 0:
        return n
    return n * fact(n-1)

#print(f'{(n := input())} = {fact(int(n))}')

'''
n = 1115
b = 1

while True:
    if n == 1 or n == 0:
        break

    b *= n
    n -= 1

print(b)

'''