# Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

import hashlib

string = 'abbracadabra'
unique_set = set()

for i in range(len(string)):
    for j in range(i + 1, len(string) + 1):
        hash_str = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
        unique_set.add(hash_str)

# исходим из того, что сама строка не является подстрокой самой же себя.
count_substring = len(unique_set) - 1
print(f'{count_substring} подстрок в строке {string}')
