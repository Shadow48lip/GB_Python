# f = open('my_file.txt')
#
# print(f.read())
#
# print(f.readlines())
# print(type(f.readlines()))
#
# lines = f.readlines()
# for line in lines:
#     # print(line, end='')
#     print(line.strip())
#
# print(f.readline())
#
# for line in f:
#     print(line.strip())

# f = open('my_file1.txt', 'w')
# f.write('qwe\nasd\nzxc')
# f.close()


# str_lines = ['str1', 'str2', 'str3']

# with open('my_file1.txt', 'w', encoding='utf-8') as f:
    # print('qwe\nasd\nzx12c', file=f)
    # f.write('Привет мир!')
    # f.writelines(str_lines)
    # f.write(',\n'.join(str_lines))

# with open('my_file12.txt', 'r+', encoding='utf-8') as f:
#     print(f.read())
#     f.write('Привет мир!')

# def my_f(file):
#     file.write()

# with open('my_file12.txt', 'r+', encoding='utf-8') as f:
#     print(f.closed)
#     print(f.name)
#     print(f.mode)
    # my_f(f)


# with open('my_file12.txt', 'w+', encoding='utf-8') as f:
#     f.write('Привет мир!\n123\n10')
#     f.seek(0)
#     print(f.read())

# import json
# # data = {'income': {'salary': 50000, 'bonus': (500, 100)}}
# # with open('Petr.json', 'w') as f:
# #     json.dump(data, f)
# with open('Petr.json') as f:
#     data = json.load(f)
#     print(data)
#     print(type(data))


import pickle
# import json
# import random
# from time import perf_counter
#
# nums = [x for x in range(10 ** 6)]
#
# start = perf_counter()
# with open('numbers.json', 'w') as f:
#     json.dump(nums, f)
# end = perf_counter()
# print(end - start)
#
#
# nums = (x for x in range(10 ** 6))
# with open('numbers.pickle', 'wb') as f:
#     pickle.dump(nums, f)
# print(end - start)


# import pickle
# chunk_size = 256
# with open('numbers.pickle', 'rb') as f:
#     binary_data = bytearray()
#     while True:
#         chunk = f.read(chunk_size)
#         if not chunk:
#             break
#         binary_data.extend(chunk)
#
# nums = pickle.loads(binary_data)
# print(type(nums), len(nums))


# txt = 'Привет'
#
# txt_binary = txt.encode(encoding='utf-8')
# txt_original = txt_binary.decode(encoding='utf-8')
#
# print(txt_binary, type(txt_binary))
# print(txt_original, type(txt_original))