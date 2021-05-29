# num1 = 5
# word = 'asd'
# var = [num1, word]
# print(type(var))
# print(type(var) == list)
# print(type(var) == int)
# print(isinstance(var, list))
# print(isinstance(var, int))
# print(dir(var))
# print(dir(a))
# print(word + '1')

# my_list1 = ['qwe', 123, True, 6560.01, 'qwe', 'q', True]
# print(id(my_list1))
# my_list2 = [1, 2, 3]
# my_list.append(50)
# my_list1.extend(my_list2)
# out_info = my_list1.pop(1)
# print(out_info)
# print(my_list1.index('qwe', 1))
# print(my_list1.count(True))
# my_list1.insert(0, 'asdasd')
# my_list1.remove(True)
# my_list1.reverse()
# print(id(my_list1))
# print(my_list1)


# my_list1 = ['qwe', 123, True, 6560.01, 'qwe', 'q', True]
# print(id(my_list1))
# my_list1.reverse()
# print(id(my_list1))
#
# print()
# my_list2 = ['qwe', 123, True, 6560.01, 'qwe', 'q', True]
# print(id(my_list2))
# my_list2 = list(reversed(my_list2))
# print(my_list2)
# print(id(my_list2))


# my_list2 = ['qwe', 123, True, 6560.01, 'qwe', 'q', True]
# print(id(my_list2))
# print(my_list2[1:])  # [start:stop:step]
# print(my_list2[1:6:2])  # [start:stop:step]
# print(my_list2[1::2])  # [start:stop:step]
# print(my_list2[::2])  # [start:stop:step]
# print(my_list2[::3])  # [start:stop:step]
# print(id(my_list2[::-1]))  # [start:stop:step]


# a = [10, 20]
# b = a.copy()
# print(id(a) == id(b))
# b.append(100)
# print(a)

# import copy
# a = [10, 20, [100, 200]]
# b = copy.deepcopy(a)
# b[2].append(300)
# print(a)

# a = 258
# b = 258
# print(a == b)

# a = ['декабрь', 'январь', 'феварль']
# a.sort()
# print(a)

# print(ord('а'))
# print(ord('я'))
# print(sorted(a))
# my_list = ['декабрь', 'январь', 'феварль']
# my_tuple = ('декабрь', 'январь', 'феварль')
# print(my_tuple.index('январь'))
# print(my_tuple.count('январь123'))

# import sys
# print(sys.getsizeof(my_list))
# print(sys.getsizeof(my_tuple))
# my_tuple[1] = 'июнь'
# print(my_tuple)

# print(ord('Я'))
# print(ord('я'))
# print(chr(1103 - 32))
# my_str = 'Иванов Иван Иванович'
# email = 'ivan@mail.ru'
# print(my_str.lower())
# print(my_str.upper())
# print(my_str.title())
# print(my_str.capitalize())
# print(email.split())
# print(email)


# my_list = ['декабрь', 'январь', 'феварль', 'июнь']
# my_str = ', '.join(my_list)
# print(my_str)

# my_str = 'Иванов Иван Иванович ы ваоыд одыл авод ылвоадывлоа дылвоа ждывало'
# surname, name, *other = my_str.split()
# print(surname)
# print(name)
# print(other)


name = 'Ivan'
surname = 'Иванов'
year = 1

old_str = 'Имя:' + name + 'Фамилия:' + surname + 'Возраст:' + str(year)
print()
print('Имя: %s Фамилия: %s Возраст: %d' % (name, surname, year))
print('Имя: {} Фамилия: {} Возраст: {}'.format(name, surname, year))
print('Имя: {1} Фамилия: {0} Возраст: {2}'.format(name, surname, year))

# new_str = f'Имя: {name:^15} Фамилия: {surname} Возраст: {year:.4f}'
new_str = f'Имя: {name:^15} Фамилия: {surname} Возраст: {year:04d}'
print(new_str)