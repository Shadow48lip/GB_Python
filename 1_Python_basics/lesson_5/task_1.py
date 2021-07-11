__author__ = 'Дмитрий Назаркин'


# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield
# *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.


# a)
def odd_nums_a(max):
    # nums = []
    for i in range(1, max + 1, 2):
        # nums.append(i)
        yield i


odd_to_15 = odd_nums_a(15)

#  лень писать 15 принтов :)
for _ in range(20):
    try:
        print(next(odd_to_15))
    except StopIteration:
        print('Закончились итерации')
        break


# b)
def odd_nums_b(max):
    nums_gen = (num for num in range(1, max + 1, 2))
    return nums_gen


odd_to_20 = odd_nums_b(20)
print(type(odd_to_20), *odd_to_20)
