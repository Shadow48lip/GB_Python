# Написать два алгоритма нахождения i-го по счёту простого числа.

import time


# Декоратор. Засекаем время выполнения
def time_func(func):
    def wrapper(*args):
        start_time = time.time()
        res = func(*args)
        end_time = time.time()
        print('Время исполнения', end_time - start_time)
        return res

    return wrapper


# Без использования «Решета Эратосфена»;

# O(n**2) так как гоняем 2 цикла, пространственная сложность минимальна, больших данных не создаем O(1)
@time_func
def no_eratosthenes(n):
    if n == 1:
        return 2
    i = 2
    c = 0

    while True:
        i += 1
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            c += 1
            if c == n:
                return i


# Используя алгоритм «Решето Эратосфена»


# O(n*9 log(log n)) предполагаемая базовая сложность алгоритма
# вся прелесть решета, как я понял, в том, что оно убивает не простые числа как бы в будущем, когда мы не проверяли их
# циклом еще. Не нашел ничего лучше как взять общий список с запасом. Плюс еще 1 на отфильровку списка для нахождения
# i-го числа. Пространственная сложность минимальна примерно так же O(n*9), так как раздуваем списки.
# Но есть некие сомнения в моих рассчетах... Никогда раньше не оценивал так код.
@time_func
def eratosthenes(n):
    if n == 1:
        return 2
    b = n * 8
    numb = [i for i in range(0, b + 1)]
    numb[0] = numb[1] = False
    for i in range(2, b):
        if numb[i]:
            for j in range(2 * i, b + 1, i):
                numb[j] = None
    res_ar = [i for i in numb if i]
    return res_ar[n - 1]


# В средним на больших вычислениях алгоритм с решетом выполняется на replit.com 0.0033 против 1.0620
num = 500
print(no_eratosthenes(num))
print(eratosthenes(num))

