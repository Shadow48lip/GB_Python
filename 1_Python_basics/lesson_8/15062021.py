# letters = {chr(code) for code in range(ord('а'), ord('я') + 1)}
# letters.add('ё')
#
#
# def name_is_valid(name):
#     if not name or set(name.lower()) - set(letters):
#         return False
#     return name.istitle()
#
# print(name_is_valid('Ваня'))
# print(name_is_valid('ваня'))
# print(name_is_valid('ванz'))
# print(name_is_valid('Ванz'))

#
# import re
# RE_NAME = re.compile(r'^[А-ЯЁ][а-я]{0,}$')
# # https://regex101.com/
#
# def name_is_valid(name):
#     return RE_NAME.match(name)
#
# print(name_is_valid('Ваня'))
# print(name_is_valid('ваня'))
# print(name_is_valid('ванz'))
# print(name_is_valid('Ванz'))


# import re
# ДД.ММ.ГГГГ

# RE_DATE = re.compile(r'^(\d{2}\.){2}\d{4}$')
# for date in ['10.25.1885', '10.25.188']:
#     assert RE_DATE.match(date), f'wrong date {date}'


# import re
# RE_DATE = re.compile(r'(?:\d{2}\.){2}\d{4}')
# txt = '10.25.1885 10.25.188 1.25.1885 10.2.1885 10.25.1885ц ф10.25.1885 10*25;1885'
# # print(RE_DATE.findall(txt))
# print(RE_DATE.search(txt))
# print(RE_DATE.match(txt))
# print(RE_DATE.finditer(txt))


# def render_input(field):
#     return f'<input id ="id_{field}" type = "text" name = "{field}">'


# username = render_input('user')
# print(username)


# def p_wrapper(func):
#     def tag_wrapper(*args, **kwargs):
#         markup = func(*args, **kwargs)
#         return f'<p>{markup}</p>'
#
#     return tag_wrapper
#
#
# @p_wrapper
# def render_input(field):
#     return f'<input id ="id_{field}" type = "text" name = "{field}">'
#
#
# username = render_input('user')
# print(username)


# def cache_f(func):
#     cache = {}
#
#     def wrapper(*args):
#         nonlocal cache
#         key = str(*args)
#         if key not in cache:
#             cache[key] = func(*args)
#         return cache[key]
#
#     return wrapper
#
# @cache_f
# def render_input(field):
#     print('call', field)
#     return f'<input id ="id_{field}" type = "text" name = "{field}">'
#
#
# user = render_input('username')
# password = render_input('password')
# user2 = render_input('username')
#
# print(user)
# print(user2)


# def cache_f(func):
#     cache = {}
#
#     def wrapper_cache(*args):
#         nonlocal cache
#         key = str(*args)
#         if key not in cache:
#             cache[key] = func(*args)
#         return cache[key]
#
#     return wrapper_cache
#
#
# def logger(func):
#     def wrapper_logger(*args):
#         result = func(*args)
#         print(f'call {func.__name__}, {args}')
#         return result
#     return wrapper_logger
#
#
# @logger
# @cache_f
# def render_input(field):
#     return f'<input id ="id_{field}" type = "text" name = "{field}">'


# user = render_input('username')
# password = render_input('password')
# user2 = render_input('username')


from functools import wraps


def some_f(func):
    @wraps(func)
    def wrapper(arg):
        print('qwe')
        return func(arg)

    return wrapper

@some_f
def calc(x):
    """some info how to calc"""
    print(x + 2)

calc(5)
print(calc.__name__)
print(calc.__doc__)