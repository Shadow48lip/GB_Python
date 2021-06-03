__author__ = 'Дмитрий Назаркин'

# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) и
# возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно
# использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном
# браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными
# величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
# аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от
# того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
# *(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая передаётся в
# ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа, какой тип данных лучше
# использовать в ответе функции?
import requests, datetime


def currency_rates(currency_code):
    data = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

    # Ищем валюту
    position = data.text.find(currency_code.upper())

    if position == -1:
        return None

    # Курс
    pos_exch_rate_start = data.text.find('<Value>', position) + 7
    pos_exch_rate_stop = data.text.find('</Value>', position)
    exchange_rate = float(data.text[pos_exch_rate_start:pos_exch_rate_stop].replace(',', '.'))

    # Дата (немного облегчу поиску задачу, умерим жадность)
    pos_date_start = data.text.find('Date="', 1, 200) + 6
    pos_date_stop = data.text.find('" name', pos_date_start, 100)
    document_date = data.text[pos_date_start:pos_date_stop]
    date_obj = datetime.datetime.strptime(document_date, '%d.%m.%Y').date()

    return date_obj, exchange_rate


# Decimal немного усложнит код и он здесь не оправдан, так как мы не ведём никаких вычислений с дробными числами
# я прочитал про непредсказуемые дроби при сложении флотов :)

eur_tuple = currency_rates('eur')
print('Функция отдает кортэж:', type(eur_tuple))
print('Объект даты:', type(eur_tuple[0]), eur_tuple[0])
print('Курс Евро:', type(eur_tuple[1]), eur_tuple[1])

usd_tuple = currency_rates('USD')
print('Курс Доллара:', usd_tuple[0], usd_tuple[1])
