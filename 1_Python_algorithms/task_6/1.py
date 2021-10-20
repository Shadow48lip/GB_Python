
import sys

print(sys.getsizeof(42)) # 28 байт занимает короткое целовек число
print(sys.getsizeof([])) # 56 байт занимает пустой массив(список)
print(sys.getsizeof([42])) # 64 байта
# 64 = (56 + 8)

print(sys.getsizeof([1,2,3,4,5,6,7,8,9,10])) #136 байт
# 136 = (56 + 8 * 10)

# 10 чисел в списке в Python
# 56 + (8 + 28) * 10 = 416 байт

#сборщики мусоров (garbage collector)
