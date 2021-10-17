# 1 Программа сложения и умножения комплексных чисел

class Cmplex:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def __add__(self, obj):
        self.sumax = self.x + obj.x
        self.sumay = self.y + obj.y
    
    def __mul__(self, obj):
        self.multx = self.x * obj.x - self.y * obj.y
        self.multy = self.y * obj.x - self.x * obj.y


x = float(input())
y = float(input())
a1 = Cmplex(x,y)

x = float(input())
y = float(input())
a2 = Cmplex(x,y)

a1 + a2
a1 * a2

print(a1.sumax, a1.sumay)

print(a1.multx, a1.multy)


x = float(input())
y = float(input())
a1 = complex(x,y)
x = float(input())
y = float(input())
a2 = complex(x,y)

summa = a1 + a2
mult = a1 * a2
print(summa, mult) 
