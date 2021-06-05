import itertools
import sys
from time import perf_counter

# print(type(nums), sys.getsizeof(nums))

# print(type(nums_gen), sys.getsizeof(nums_gen))


# start = perf_counter()
# print(start, type(start))
# nums = []
# for num in range(1, 10 ** 6 + 1, 2):
#     nums.append(num ** 2)
# sum(nums)
# end = perf_counter()
# print(end)
# print(end - start)

# start = perf_counter()
# nums_gen = (num ** 2 for num in range(1, 10 ** 6 + 1, 2))
# sum(nums_gen)
# end = perf_counter()
# print(end - start)

nums_gen = (num ** 2 for num in range(1, 10 ** 6 + 1, 2))
print(nums_gen)
# for i, num in enumerate(nums_gen):
#     pass

print(next(nums_gen))
print(next(nums_gen))
# dfdf

# print(*itertools.islice(nums_gen, 1))


# nums_gen = (num ** 2 for num in range(1, 10 ** 6 + 1, 2))
# print(sum(nums_gen))
# print(sum(nums_gen))

# eng = (chr(code) for code in range(ord('a'), ord('z') + 1))
# print(list(eng))


# def nums_generator(max_num):
#     for num in range(1, max_num + 1, 2):
#         yield num ** 2
#
#
# nums_gen1 = nums_generator(10 ** 6)
# nums_gen2 = nums_generator(100)
# print(type(nums_gen1), sys.getsizeof(nums_gen1))
# print(sum(nums_gen1))

# new_list = [x for x in range(1, 10 ** 6) if x > 868940]
# print(new_list)

# matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix2 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
#
# matrix_sum = [[cell1 + cell2 for cell1, cell2 in zip(row1, row2)]
#               for row1, row2, in zip(matrix1, matrix2)
#               ]
# print(matrix_sum)

# nums = {num: num ** 2 for num in range(10) if num % 2 == 0}
# print(nums)

# basket = ['red', 'green', 'blue', 'green', 'green', 'blue', 'green', 'yellow']
# out_basket = []
# [out_basket.append(x) for x in basket if x not in out_basket]
# print(out_basket)

# print(len(set(basket)))

my_set1 = {1, 2, 3}
my_set2 = {3, 4, 5}

# my_set.discard(10)
# my_set.remove(10)
# print(my_set1 - my_set2)
print(my_set1 & my_set2)
# print(my_set1.intersection(my_set2))


print(my_set1 | my_set2)
print(my_set1.union(my_set2))

# my_set = set()
# my_set = {}
# print(my_set1)

# my_set2 = frozenset()

# import random
# nums = {num for num in range(10) if num % 2 == 0}
# nums = {random.randint(1, 10) for _ in range(14)}
# print(nums, type(nums))

# basket = ['red', 'green', 'blue', '0']
# a = frozenset(basket)
# print(a)