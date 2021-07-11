__author__ = 'Дмитрий Назаркин'

# Есть два списка:
# ....
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов,
# чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)
# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать, в каких ситуациях
# генератор даст эффект.

from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

# zip_longest вервнет (<tutor>, None) если в tutors будет больше значений, чем в klasses
schoolchilds = (child for child in zip_longest(tutors, klasses) if child[0])
print(next(schoolchilds))
print(next(schoolchilds))
print(next(schoolchilds))
print(next(schoolchilds))
print(next(schoolchilds))
print(next(schoolchilds))
print(next(schoolchilds))
# тут вернет исключение - генератор всё
print(next(schoolchilds))
