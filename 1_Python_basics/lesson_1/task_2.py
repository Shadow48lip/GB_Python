__author__ = 'Дмитрий Назаркин'
# Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
# a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
# b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# c. * Решить задачу под пунктом b, не создавая новый список.


cube_digits = []
for dig in range(1, 1000, 2):
    cube_digits.append(dig ** 3)
print(cube_digits)

# ответ на первый вопрос (а)
sum_numbers_a = 0
sum_numbers_b = 0

# Перебор списка с кубами для нахождения суммы чисел
for cube in cube_digits:
    sum_numbers = 0
    original_number = cube

    # пункт - а
    for splitter in reversed(range(10)):
        # делитель
        splitter = 10 ** splitter
        # один знак числа
        number = cube // splitter

        if number > 0:
            # print(number, splitter)
            # print('Cube', cube, 'Split', splitter)
            sum_numbers += number
            cube -= number * splitter

    # считаем сумму для вопроса под литерой - а
    if sum_numbers > 0 and not sum_numbers % 7:
        sum_numbers_a += sum_numbers


    # пункт - b,c
    sum_numbers2 = 0
    original_number += 17
    cube = original_number

    for splitter in reversed(range(10)):
        # делитель
        splitter = 10 ** splitter
        # один знак числа
        number = cube // splitter

        if number > 0:
            # print(number, splitter)
            # print('Cube', cube, 'Split', splitter)
            sum_numbers2 += number
            cube -= number * splitter

    # if sum_numbers2 > 0:
    #     print('Число', original_number, 'его сумма', sum_numbers2)

    # считаем сумму для вопроса под литерой - а
    if sum_numbers2 > 0 and not sum_numbers2 % 7:
        sum_numbers_b += sum_numbers2

print('Ответ на вопрос к задаче 2, пункт "а":', sum_numbers_a)
print('Ответ на вопрос к задаче 2, пункт "b,c":', sum_numbers_b)
