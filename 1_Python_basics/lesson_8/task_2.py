__author__ = 'Дмитрий Назаркин'

# *(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) для получения
# информации вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>,
# <response_size>),

import re
import requests

response = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
# response = requests.get('https://www.lipsat.ru')
if response.status_code != 200:
    print('Документ не скачался')
    exit(1)

RE_LOG = re.compile(r'^([\d\.]+).+?\[(.+?)\]\s+\"(\w+)\s([^\s]+).+?(\d{3})\s(\d+)', flags=re.MULTILINE)

# line = RE_LOG.findall(response.text)
# print(list(lines))

lines = RE_LOG.finditer(response.text)
for line in lines:
    print(line[1], line[2], line[3], line[4], line[5], line[6])
