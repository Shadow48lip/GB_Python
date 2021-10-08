# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве

from random import randint

arr = [randint(-100, 100) for i in range(50)]
print(arr)

f = -1000

for i in arr:
    if 0 > i > f:
        f = i

print('Индекс макс. отрицательного элемента ', arr.index(f), ', а его значение', f)
