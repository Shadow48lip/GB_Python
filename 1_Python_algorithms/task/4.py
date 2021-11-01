#Задача 4. Проверим делимость одного числа на другое
def func_main_easy(value1, value2):
    temp = value1 % value2
    if temp > 0:
        return False
    return True


def func_main(value1, value2):
    return value1 % value2 == 0



def test():
    assert func_main(6, 4) == False, 'incorect'
    assert func_main(6, 3) == True, 'incorect'
    assert func_main(0, 4) == True, 'incorect'


test()
#func_main(int(input()))