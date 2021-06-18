__author__ = 'Дмитрий Назаркин'

# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и
# почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.

import re

# ВОПРОС - имеет ли смысл re.compile()? внутри функции он же создается каждый раз заново? Если вынести выше, то да.
# Так же читал, что интерпритатор сам кеширует последние шаблоны.
def email_parse(email):
    match =  re.fullmatch(r'^(\w+)@(\w+\.[a-z]{2})$', email.lower())
    if not match:
        msg = 'wrong email: ' + email
        raise ValueError(msg)

    return {'username': match[1], 'domain': match[2]}

# print(list(email_parse('Dmitriy@yandex.ru')))
print(email_parse('Dmitriy@yandex.ru'))
print(email_parse('dmitriy@yandexru'))





