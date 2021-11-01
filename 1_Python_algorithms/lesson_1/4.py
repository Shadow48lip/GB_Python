# Написать программу, которая генерирует в указанных пользователем границах
# случайное целое число,
# случайное вещественное число,
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить
# случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ
# алфавита от 'a' до 'f' включительно.
import random

print('Выберите что хотите сгенерировать\n1 - случайное целое число\n2 - случайное вещественное число\n'
      '3 - случайный символ')
select_type = int(input('введите 1, 2 или 3: '))

if select_type == 1:
    user_range_1, user_range_2 = map(int, input('Задайте границы выборки через пробел: ').split())
    if user_range_1 > user_range_2:
        print('Первое число должно быть меньше второго.')
        exit(1)

    result_random = random.randint(user_range_1, user_range_2)
    print(f'Случайное целое число: {result_random}')

elif select_type == 2:
    user_range_1, user_range_2 = map(float, input('Задайте границы выборки через пробел: ').split())
    if user_range_1 > user_range_2:
        print('Первое число должно быть меньше второго.')
        exit(1)

    result_random = random.uniform(user_range_1, user_range_2)
    print(f'Случайное вещественное число: {result_random}')

elif select_type == 3:
    user_range_1, user_range_2 = map(str, input('Задайте крайние символы через пробел: ').split())
    code_1 = ord(user_range_1)
    code_2 = ord(user_range_2)

    if code_1 > code_2:
        print('Первый символ алфавита должен стоять раньше второго.')
        exit(1)

    result_random = chr(random.randint(code_1, code_2))
    print(f'Случайное символ в диапазоне от {user_range_1} до {user_range_2}: {result_random}')



else:
    print('Ничего не выбрано')
