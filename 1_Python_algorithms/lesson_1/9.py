# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

dig_1, dig_2, dig_3 = map(int, input('Введите три числа через пробел: ').split())

if dig_2 < dig_1 < dig_3 or dig_2 > dig_1 > dig_3:
    print(f'{dig_1} среднее число')
elif dig_1 < dig_2 < dig_3 or dig_1 > dig_2 > dig_3:
    print(f'{dig_2} среднее число')
else:
    print(f'{dig_3} среднее число')
