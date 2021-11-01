# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м
# включительно. Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.


codes = [x for x in range(32, 128)]
line_size = 10

for pos in range(len(codes) // line_size + 1):
    pos_start = pos * line_size
    pos_stop = pos_start + line_size
    codes_line = codes[pos_start:pos_stop]

    for code in codes_line:
        print(f'{code} - {chr(code)}', end=' | ')
    print('')
