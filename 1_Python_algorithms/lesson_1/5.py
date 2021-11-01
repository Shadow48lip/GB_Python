# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
# ord(символ)	Символ в его код ASCII
# chr(число)	Код ASCII в символ

letter_1 = str(input('введите первую букву английского алфавита: ')).lower()
letter_2 = str(input('введите вторую букву: ')).lower()
# letter_1, letter_2 = map(str, input('введите две буквы: ').split())

if len(letter_1) != 1 or len(letter_2) != 1:
    print('Должно быть по одной букве. Повторите.')
    exit(1)

# Точка отсчета
start_position = ord('a') - 1
# Коды символов
code_1 = ord(letter_1)
code_2 = ord(letter_2)

# Позиции
letter_1_pos = code_1 - start_position
letter_2_pos = code_2 - start_position

print(f'позиция символа {letter_1}: {letter_1_pos}\nпозиция символа {letter_2}: {letter_2_pos}')

# Сколько между ними символов (можно было решить по модулю, но тогда бы без условия обошлись)
if letter_1_pos < letter_2_pos:
    difference_letter = letter_2_pos - letter_1_pos - 1
else:
    difference_letter = letter_1_pos - letter_2_pos - 1

print(f'между ними {difference_letter} букв(ы)')
