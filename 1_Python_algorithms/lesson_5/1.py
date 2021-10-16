# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

fabric_nums = int(input('Сколько будет предприятий: '))

fabrics = {}
avg_value = 0

for i in range(fabric_nums):
    fabric_name = str(input(f'Имя предприятия {i+1}: '))
    fabric_value = sum(map(int, input('Прибыль за 4 квар. через пробел: ').split()))

    fabrics[fabric_name] = fabric_value
    avg_value += fabric_value

avg_value /= fabric_nums
print (f'Средняя годовая прибыль по всем предприятиям: {avg_value}')


avg_high = []
avg_low = []

for i in fabrics:
    if fabrics[i] > avg_value:
        avg_high.append(i)
    else:
        avg_low.append(i)

print(f'Прибыль выше среднего у: {avg_high}')
print(f'Прибыль ниже среднего у: {avg_low}')