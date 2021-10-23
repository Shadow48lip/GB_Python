
# https://www.youtube.com/watch?v=ywWBy6J5gz8

#O(n^2) - худший случай
#O(n* log2n) - средний случай
def qsort(lst):

    def qsort_inplace(lst, start=0, end=None):
        if end is None:
            end = len(lst)
        if end - start > 1:
            pivot = pivot_inplace(lst, start, end)
            qsort_inplace(lst, start, pivot)
            qsort_inplace(lst, pivot + 1, end)
    
    def pivot_inplace(lst, start, end):
        pivot = lst[start]
        x = start + 1
        y = end - 1

        while True:
            while (x <= y) and lst[x] <= pivot:
                x += 1
            while (x <= y) and lst[y] >= pivot:
                y -= 1
            
            if  x <= y:
                lst[y], lst[x] = lst[x], lst[y]
            else:
                lst[start], lst[y] = lst[y], lst[start]
                return y
    
    qsort_inplace(lst)
    return lst




lst = [54,3,3,4,5,2,24,2342,13413,134134,1,34]
print(qsort(lst))

    