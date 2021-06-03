# import lib.hello_module as hm
# import hello_module as hm
# from hello_module import say_hello
# from hello_module import *

# hm.say_hello('Ivan')
# print(hm.pow(10))

# say_hello()
# say_hello('Ivan')
# print(pow(10, 6))

# def say_hello(name):
#     print(name + 'qwe')
# import requests
# from requests import get
# response = get('http://geekbrains.ru')
# print(response.headers)
# print(response.status_code)
# print(response.content)
# print(response.close)


# import sys
# import time
import argparse
# folder1, folder2 = sys.argv[1:]
# print(f'copy from {folder1} to {folder2}...')
# time.sleep(2)
# print('done')

# import time
#
# nums = []
# for num in range(1, 10 ** 6 + 1):
#     nums.append(num)
#
# start = time.perf_counter()
# nums_sum = 0
# i = 0
# while i < len(nums):
#     nums_sum += nums[i]
#     i += 1
# finish = time.perf_counter()
# print(finish - start, nums_sum)
#
# start = time.perf_counter()
# nums_sum = 0
# for num in nums:
#     nums_sum += num
# finish = time.perf_counter()
# print(finish - start, nums_sum)
#
# start = time.perf_counter()
# nums_sum = sum(nums)
# finish = time.perf_counter()
# print(finish - start, nums_sum)

from datetime import datetime, timedelta

# date_1 = datetime(year=2020, month=12, day=5)
# date_2 = datetime(year=2019, month=12, day=4)
# date_delta = date_1 - date_2
# print(date_delta.days)
# print(date_delta.seconds)


user_created = datetime(year=2020, month=12, day=5, hour=12, minute=52, second=6)
print(str(datetime))
activation_period = timedelta(days=190)
current_time = datetime.now()
print('www', current_time, activation_period)

if current_time < user_created + activation_period:
    print(f'Осталось {user_created + activation_period - current_time}')
else:
    print('время вышло')

