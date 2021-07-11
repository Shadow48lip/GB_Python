# user_1 = ['Иван', 30]
# user_2 = ['Oleg', 40]

user_3 = {'name': 'Ivan', 'age': 30, 'phone': 929091090219}
# dict
# print(user_3['age'])
# print(user_3['qwe'])
# print(user_3.get('age'))
# print(user_3.get('qwe', 100))
# print(user_3.get('age', 100))

user_1 = {'name': 'Ivan', 'age': 30, 'phone': 929091090219}

# user_2 = {'name': 'asd'}
# user_1.update(user_2)
# print(user_1)
print(user_3.setdefault('adress', 'Россия'))
# print(user_3.setdefault('age', '20'))
print(user_3)
# user_3['qwe'] = 'asd'
# print(user_3)
# user_1.update(user_2)
# print(user_1)
# print(user_1.popitem())
# print(user_1)
# print(user_1.pop('age', None))
# print(user_1)

# for key in user_1.keys():
#     print(key)

# for val in user_1.values():
#     print(val)

# for key, val in user_1.items():
#     print(key, val)

# print('name' in user_1)

# DRY

# def say_hello(name):
#     print(name, 'hello')
#
#
# say_hello('Ivan')
# say_hello('Oleg')


# def average(nums):
#     out = sum(nums) / len(nums)
#     return out

# def average(nums):
#     pass


# answer = average([1, 2, 3, 4, 5])
# print(answer)

# def print(text):
#     pass
#
# print('100')

# def qwe():
#     print('qwe')
#
# a = qwe
# qwe()
# a()

# def qwe(name, surname):
#     """Эта функция ничего не делает"""
#     pass

# def qwe(name, surname):
#     """
#     Эта функция ничего не делает
#     name: str
#     surname: str
#     return: None
#     """
#     pass
#
# qwe('name', 'qwe')


# x = 100
# def qwe():
#     x = 10
# qwe()
# print(x)

# x = 100
#
#
# def qwe():
#     print(x)
#
#
# qwe()


# z = 12312
# def qwe():
#     print(x)

# x = 100
# def qwe():
#     global x
#     x = 99
# qwe()
# print(x)

# x = 100


# def qwe(x):
#     x += 1
#     return x


# x = qwe(x)
# x = qwe(100000)
# print(x)


# def my_f(name, surname=None):
#     print(name, surname)
#
# my_f('Ivan', 'Ivanov')
# my_f('Ivan')


# def my_f(name, *args):
#     print(name, args)
#
# my_f('Ivan', 10, 20, 30)
# my_f('Ivan')
# my_f('Ivan', 10, 20, 30, 40, 50)


# def my_f(name, surname, age):
#     print(name, surname, age)
#
#
# my_f(name='Ivan', age=30, surname='Ivanov')


# def my_f(name, **kwargs):
#     print(name, kwargs)
#
# my_f('Ivan', age=30, surname='Ivanov')


import random

# print(random.random())
# print(random.randint(0, 10))
# print(random.randrange(0, 10, 3))
print(random.choice(['qwe', 'asd', 'zxc']))

from itertools import zip_longest
names = ['Алексей', 'Дмитрий', 'Татьяна']
ages = [50, 4]

# user_5 = zip(names, ages)
# print(list(user_5))

#
# print(list(zip(names, ages)))
# for name, age in zip_longest(names, ages, fillvalue=''):
#     print(name, age)
# def qwe(x):
#     return x ** 3 + 1

# def qwe2(x):
#     return x >= 0

data = [4, -5, 10, -50]
# new_list = []
# for num in data:
#     new_list.append(qwe(num))
# print(new_list)

# a = lambda x: x ** 3 + 1
# print(list(map(a, data)))
# print(list(filter(lambda x: x >= 0, data)))
# print(a(10))