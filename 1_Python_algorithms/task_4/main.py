import time


def time_func(func):
    def wrapper():
        start_time = time.time()
        res = func()
        end_time =  time.time()
        print('Время исполнения', end_time-start_time)
        return res
    return wrapper


arr, value = list(range(1000000)), 999999

@time_func
def binary_search():
    first = 0
    last = len(arr) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if arr[mid] == value:
            index = mid
        else:
            if value < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index


@time_func
def lenear_search():
    for i in range(len(arr)):
        if arr[i] == value:
            return i



binary_search()

lenear_search()