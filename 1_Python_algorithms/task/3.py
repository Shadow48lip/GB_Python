#Задача 3. Вычислить значение функции y=f(x)
def func_main(value):
    if value < 0:
        return 2 ** (-value)
    elif value > 0:
        return 1/value
    else:
        return 1 


def test():
    assert func_main(-7) == 128, 'incorect 1'
    assert func_main(0) == 1, 'incorect 2'
    assert 0.5 <= func_main(2) < 0.6, 'incorect 3'


test()
#func_main(int(input()))