


import time

import random

#O(n^2)
def bubble_sort(mas):
    j = 1
    while j < len(mas):
        for i in range(len(mas)-j):
            if mas[i] > mas[i+1]:
                mas[i], mas[i+1] = mas[i+1], mas[i]
        j += 1
    return mas

def insert_sort(mas):
    for i in range(len(mas)):
        v = i
        for j in range(i+1, len(mas)):
            if mas[v] > mas[j]:
                v = j
        if v != i:
            mas[i], mas[v] = mas[v], mas[i]
    return mas

def qsort(lst):

    def qsort_inplace(lst, start=0, end=None):
        if end is None:
            end = len(lst)
        if end - start > 1:
            pivot = pivot_inplace(lst, start, end)
            qsort_inplace(lst, start, pivot)
            qsort_inplace(lst, pivot + 1, end)
    

    def pivot_inplace(lst, start, end):
        pivot = lst[start]
        x = start + 1
        y = end - 1

        while True:
            while (x <= y) and lst[x] <= pivot:
                x += 1
            while (x <= y) and lst[y] >= pivot:
                y -= 1
            
            if  x <= y:
                lst[y], lst[x] = lst[x], lst[y]
            else:
                lst[start], lst[y] = lst[y], lst[start]
                return y
    
    qsort_inplace(lst)
    return lst


mas = [random.randint(1000,100000) for i in range(100000)]

print('gen list done')

a = time.time()
qsort(mas.copy())
print(time.time() - a)

a = time.time()
insert_sort(mas.copy())
print(time.time() - a)

a = time.time()
bubble_sort(mas.copy())
print(time.time() - a)


