__author__ = 'Дмитрий Назаркин'

# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список
# кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
#
# *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
from collections import Counter

# a)
parsed_data = []

with open("nginx_logs.txt", "r") as f:
    for line in f:
        ip_addr, _, _, _, _, req_type, req_resource, *args = line.strip().split()
        req_type = req_type.strip('"')

        parsed_data.append((ip_addr, req_type, req_resource))

print(parsed_data)

# Еще один вариант. Отсортировать массив по значениям и вывести чеерез срез ТОП-5
#         spam_dict.setdefault(splitted[0], 0)
#         spam_dict[splitted[0]] += 1
# spam_dict = sorted(parsed_data.items(), key=lambda x: x[1], reverse=True)
# print(spam_dict[:5])  # Not only one spamer

# b)
flud_data = []

with open("nginx_logs.txt", "r") as f:
    for line in f:
        ip_addr, *args = line.strip().split()
        flud_data.append(ip_addr)

# В отличии от itertools.groupby функция Counter сразу дает нам отсортированный словарь
top_counters = Counter(flud_data).most_common(1)
flud_person = top_counters[0]
print(f'Чаще всего обращался IP: {flud_person[0]}, {flud_person[1]} раз.')

# print(flud_data)
