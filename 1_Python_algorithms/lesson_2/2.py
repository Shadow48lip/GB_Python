# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

dig = str(input('введите число: '))
evens = []
not_evens = []

for i in dig:
    i = int(i)

    if not i % 2:
        evens.append(i)
    else:
        not_evens.append(i)

print(f'{len(evens)} четных {evens}')
print(f'{len(not_evens)} не четных {not_evens}')
