__author__ = 'Дмитрий Назаркин'
# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до
# и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для
# чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное:
# дополнить числа до двух разрядов нулём!
# *(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят,
# in place). Эта задача намного серьёзнее, чем может сначала показаться.


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# Более заморочный вариант без создания списков
len_list = len(my_list)
start = 0

while start < len_list:
    i = my_list[start]

    if 48 <= ord(i[-1]) <= 57:

        if i[0] == '+':
            my_list[start] = f'+{int(i):02d}'
        else:
            my_list[start] = f'{int(i):02d}'

        my_list.insert(start, ' "')
        my_list.insert(start + 2, '"')

        start += 3
        len_list += 2
    else:
        # Проставляем прблеы сами, без помощи .join()
        if start != 0:
            my_list[start] = f' {i}'
        start += 1

print(my_list)

# Более простой вариант с создание копии списка.
# for i in my_list.copy():
#     if 48 <= ord(i[-1]) <= 57:
#         my_list.insert(my_list.index(i), '"')
#         my_list.insert(my_list.index(i) + 1, '"')
#
#         if i[0] == '+':
#             my_list[my_list.index(i)] = f'+{int(i):02d}'
#         else:
#             my_list[my_list.index(i)] = f'{int(i):02d}'

# Из списка в строку
my_list_str = ''.join(my_list)

# Пробелы между ковычками и числом убраны!
print(my_list_str)
