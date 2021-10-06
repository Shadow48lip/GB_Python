# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

digits = tuple(map(int, input('введите натуральные числа через пробел: ').split()))


def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum


max_sum = max_dig = 0

for i in digits:
    current_sum = sum_of_digits(i)
    if current_sum > max_sum:
        max_sum = current_sum
        max_dig = i

print(f'число {max_dig} и его сумма {max_sum}')
