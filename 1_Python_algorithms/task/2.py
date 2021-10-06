#Задача 2. Сравниваем числа и находим максимум
def func(value1, value2, value3):
    if value1 >= value2 and value1 >= value3:
        return (value1)
    elif value2 >= value1 and value2 >= value3:
        return(value2)
    else:
        return(value3)

def test():
    assert func(1,2,3) == 3, 'incorrect'
    assert func(1,3,1) == 3, 'incorrect'
    assert func(3,2,1) == 3, 'incorrect'
    assert func(3,3,3) == 3, 'incorrect'

#value1, value2, value3 = map(int, input().split(' '))

test()