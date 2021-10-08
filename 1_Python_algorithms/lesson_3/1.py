# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

digits = [x for x in range(2, 100)]
dividers = {x: 0 for x in range(2, 10)}

for i in digits:
    for d, count in dividers.items():
        if i % d == 0:
            dividers[d] += 1

print(dividers)
