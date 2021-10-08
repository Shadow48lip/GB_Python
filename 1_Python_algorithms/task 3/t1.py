



DATA = ['+', '-', '*', '/']



def calc(args):
    _res = ''
    for i in range(len(args)):
        if i % 2 == 1:
            if args[i] not in DATA:
                raise NameError
        _res += args[i]
    return eval(_res)


a = input()
p = []

while a != '=':
    p.append(a)
    a = input()

if p[-1] in DATA:
    p = p[:len(p)-1]

print(*p, end=' = ')

print(calc(p))




#'1', '+', '2', '+', '3', '+', '4', '+','5', '+', '3', '+', '2'