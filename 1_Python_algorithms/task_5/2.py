#Задача 2. Определить студентов с баллом выше среднего

suds = {}

n = int(input())
s = 0

for i in range(n):
    sname = input()
    point = int(input())
    suds[sname] = point
    s += point

avrg = s / n
print(avrg)

for i in suds:
    if suds[i] > avrg:
        print(i, suds[i])
