#O(n^2) - худший случай
def insert_sort(mas): # сортировка выбором, а не вставками.
    for i in range(len(mas)):
        v = i
        for j in range(i+1, len(mas)):
            if mas[v] > mas[j]:
                # print(mas[v], mas[j])
                v = j
        if v != i:
            mas[i], mas[v] = mas[v], mas[i]
            # print(mas)
    return mas



l = [54,3,3,4,5,2,24,2342,13413,134134,1,34]

print(insert_sort(l))

# а вот это вставками
def insertion_sort(array_to_sort):
    a = array_to_sort
    for i in range(len(a)):
        v = a[i]
        j = i
        while (a[j-1] > v) and (j > 0):
          print(f'{a[j-1]} > {v}')
          a[j] = a[j-1]
          j = j - 1
        a[j] = v
        print(i, a)
    return a