#Задача 3. Изменение данных о товарах

from pprint import pprint

data = [
    {
        'id': 1,
        'name': 'манговое',
        'price': 20
    },
    {
        'id': 2,
        'name': 'клубничное',
        'price': 30
    },
    {
        'id': 3,
        'name': 'ореховое',
        'price': 50
    },
]

new_price = int(input())
for i in data:
    i['price'] += i['price'] / 100 * new_price

pprint(data)