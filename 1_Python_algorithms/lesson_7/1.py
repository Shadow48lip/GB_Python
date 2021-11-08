# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована
# в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

from random import randint


def bubble_sort(li):
    n = 1
    while n < len(li):
        f = 0
        for i in range(len(li) - n):
            if li[i] < li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
                f = 1
        if f == 0:  # улучшил алгоритм - когда за весь цикл ничего не двинули, то значит уже все отсортировано
            break
        n += 1
    return li


arr = [randint(-100, 100) for i in range(30)]

print(arr)

print(bubble_sort(arr.copy()))