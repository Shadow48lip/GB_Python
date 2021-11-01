# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

letter_num = int(input('введите номер буквы в анлийском алфавите: '))
if 1 > letter_num or letter_num > 26:
    print(f'В английском алфавите не буквы под номером {letter_num}')
    exit(1)

start_position = ord('a') - 1
letter_result = chr(start_position + letter_num)

print(f'это буква: {letter_result}')
