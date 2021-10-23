

data = [
    ['яблоко', 80],
    ['аплеьсин', 80],
    ['арбуз', 20],
    ['якорь', 100]
]



res = sorted(data, key=lambda x: (x[-1], x[0]))

print(res)


res = sorted(data, key=lambda x: (x[0], x[-1]))

print(res)