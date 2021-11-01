"""
Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
а должна запрашивать новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке
и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0
в качестве делителя.
"""


def request_operation():
    allow_operations = ['0', '+', '-', '*', '/']

    operation = str(input('знак операции или 0 для прекращения: '))

    if operation not in allow_operations:
        print(f'-- допустимые значения операции {allow_operations}, еще раз --')
        operation = request_operation()

    return operation


while True:
    dig1, dig2 = map(int, input('введите два числа: ').split())
    operation = request_operation()

    if operation == '0':
        break
    elif operation == '/' and dig2 == 0:
        print('нельзя делить на ноль!')
    else:
        # if operation == '+':
        #     res = dig1 + dig2
        # elif operation == '-':
        #     res = dig1 - dig2
        # elif operation == '*':
        #     res = dig1 * dig2
        # else:
        #     res = dig1 / dig2

        res = eval(f'{dig1} {operation} {dig2}')

    print(f'{dig1} {operation} {dig2} = {res}')
    print('продолжаем...')
