#Задача 4. Принадлежит ли дата диапазону времени
data_time = [
    {
        'year': 2003, # 1
        'month': 12,
    },
    {
        'year': 2014, # 2
        'month': 6,
    },
    {
        'year': 2020, # 3
        'month': 1,
    },
]

new_dir = {}
new_dir['year'] = int(input())
new_dir['month'] = int(input())

k_y = 1


for i in data_time:
    if i['year'] < new_dir['year']:
        k_y += 1
    elif i['year'] == new_dir['year']:
        if i['month'] <= new_dir['month']:
            k_y += 1
        

print(k_y)