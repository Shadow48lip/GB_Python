# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

user_digit = str(input('введите трехзначное число: '))

# оказывается циклы нельзя
# check_sum = 0  # сумма всех цифр конкретного числа
# ckeck_multiple = 1  # произведение
# for one_digit in str(user_digit):
#     check_sum += int(one_digit)
#     ckeck_multiple *= int(one_digit)

check_sum = int(user_digit[0]) + int(user_digit[1]) + int(user_digit[2]) # сумма всех цифр
ckeck_multiple = int(user_digit[0]) * int(user_digit[1]) * int(user_digit[2])  # произведение

print(f'Сумма чисел {user_digit} равна {check_sum}')
print(f'Произведение чисел {user_digit} равна {ckeck_multiple}')
