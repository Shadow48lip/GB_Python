__author__ = 'Дмитрий Назаркин'

# Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать
# исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5


def val_checker(validator):
    def _val_checker(func):
        def wrapper_logger(*args):
            result = func(*args)
            if not validator(*args):
                raise ValueError(f'Wrong val {args[0]}')

            return result
        return wrapper_logger
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

# Маскировка декоратора отработана в task_3.py

print(calc_cube(3))
print(calc_cube(-3))
