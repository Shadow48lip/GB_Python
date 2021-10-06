#Задача 1. IOT system
milk = False
hlop = False
eggs = False

print('Do you have a milk?')
put = input()
if put:
    milk = True
print('Do you have a hlop?')
put = input()
if put:
    hlop = True
print('Do you have a eggs?')
put = input()
if put:
    eggs = True



if milk and hlop or eggs:
    if eggs:
        if milk:
            breakfast = 'omlet'
        else:
            breakfast = 'eggs'
    else:
        breakfast = 'milk with hlop'

else:
    if milk:
        breakfast = 'milk'
    elif hlop:
        breakfast = 'hlop'
    else:
        breakfast = 'empty'


print(breakfast)