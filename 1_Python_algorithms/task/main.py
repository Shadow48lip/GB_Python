
#Задача 4. Перевести байты в килобайты или наоборот
def func_main(value, st):
    if st == 'b':
        temp = value % 1024
        if temp > 0:
            return value / 1024
        else:
            return value // 1024
    else:
        return 1024 * value


def test():
    assert func_main(1024, 'b') == 1, 'incorrect'
    assert 0.976 < func_main(1000, 'b') < 0.977, 'incorrect'
    assert 1.074 < func_main(1100, 'b') < 1.075, 'incorrect'
    assert func_main(1, 'k') == 1024, 'incorrect'
    assert func_main(2, 'k') == 2048, 'incorrect'
    assert func_main(0, 'k') == 0, 'incorrect'
    print('OK')


test()


