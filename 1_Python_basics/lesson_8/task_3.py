__author__ = 'Дмитрий Назаркин'

# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
#
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения
# функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора?
# Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

from functools import wraps

def type_logger(func):
    # Маскировка работы декоратора
    @wraps(func)

    def wrapper_logger(*args, **kwargs):
        result = func(*args, **kwargs)
        logs = []
        for arg in args:
            logs.append(f'{arg}: {type(arg)}')
        print(f'LOGS function "{func.__name__}": {str(logs)}')
        return result
    return wrapper_logger


@type_logger
def calc_cube(x, y, z):
   return x ** 3 + y ** 3 + z ** 3

print(calc_cube(5, 7, 10))
print(calc_cube.__name__)

