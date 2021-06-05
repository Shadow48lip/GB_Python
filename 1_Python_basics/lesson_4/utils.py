# Utilites module
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


if __name__ == '__main__':

    print(currency_rates('AMD'))
