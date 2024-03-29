__author__ = 'Дмитрий Назаркин'

# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список
# с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
#
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [num for num in src if src.count(num) == 1]
print(result)

# через генератор
result_gn = (num for num in src if src.count(num) == 1)
print(*result_gn)