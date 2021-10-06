# Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6. Выполнить над числом 5
# побитовый сдвиг вправо и влево на два знака.

dig_1 = 5
dig_2 = 6

# Побитовое И
bit_and = dig_1 & dig_2
print(f'Побитовое И для чисел {dig_1} и {dig_2} равен {bit_and}')

# Побитовое ИЛИ
bit_or = dig_1 | dig_2
print(f'Побитовое ИЛИ для чисел {dig_1} и {dig_2} равен {bit_or}')

# Побитовое исключающее ИЛИ
bit_xor = dig_1 ^ dig_2
print(f'Побитовое исключающее ИЛИ для чисел {dig_1} и {dig_2} равен {bit_xor}')

# Битовое ОТРИЦАНИЕ (NOT)
bit_not_dig_1 = ~ dig_1
bit_not_dig_2 = ~ dig_2
print(f'Битовое ОТРИЦАНИЕ для чисела {dig_1} равно {bit_not_dig_1}, для {dig_2} равен {bit_not_dig_2}')

# Побитовый сдвиг вправо на 2 знака
bit_shift_r = dig_1 >> 2
print(f'Побитовый сдвиг вправо на два знака для числа{dig_1} равен {bit_shift_r}')

# Побитовый сдвиг влево на 2 знака
bit_shift_l = dig_1 << 2
print(f'Побитовый сдвиг влево на два знака для числа{dig_1} равен {bit_shift_l}')
