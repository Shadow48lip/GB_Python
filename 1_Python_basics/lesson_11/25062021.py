#
# class DataBase:
#     # def __init__(self, z, x, c, v, b):
#     #     pass
#
#     @staticmethod
#     def connect(ip=None):
#         print('connect', ip)
#
#     def select(self):
#         self.x = 0
#         print('select')


# c = DataBase()
# c.select()

# DataBase.connect(ip='125.16.1.0')
# DataBase.connect()


# class MyClass:
#     x = 0
#
#     @classmethod
#     def my_method(cls):
#         print(cls.x)
#         cls().qwe()
#
#     def qwe(self):
#         print('qwe')
#
# # a = MyClass()
# # a.my_method()
# # print(MyClass)
# MyClass.my_method()


class Customer:
    """Это класс покупатель"""

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


# john = Customer('John', 656546541)
# john.x = 0
# print(john.__dict__)
# print(hasattr(john, 'name'))
# print(hasattr(john, 'sadas'))
# print(john.__doc__)
# a = 5
# print(a.__doc__)
# print(john.__class__)
# print(Customer)
# print(john.__class__.__name__)
# print(john.__module__)


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name}, {self.surname}'


class Teacher(Person):
    def to_teach(self, subj, *pupils):
        for pupil in pupils:
            pupil.to_take(subj)


class Pupil(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.knowledge = []

    def to_take(self, subj):
        self.knowledge.append(subj)


class Subject:
    def __init__(self, *subjects):
        self.subjects = subjects

    def __str__(self):
        return f'{self.subjects}'


s = Subject('math', 'physics')
t = Teacher('Ivan', 'Ivanov')

p1 = Pupil('Petr', 'Petrov')
p2 = Pupil('Sidr', 'Sidorov')
p3 = Pupil('Dmitiy', 'Dmitriev')
#
# t.to_teach(s, p1, p2)
# print(p1.knowledge)
# print(p2.knowledge)
# print(p3.knowledge)


# class BelowZero(Exception):
#     pass
#
# try:
#     if int(input()) < 0:
#         raise BelowZero
#
# except BelowZero:
#     print('ниже нуля')


# class my_perfect_dict(dict):
#     def qwe(self):
#         pass
#
# my_perfect_dict().qwe()


# import psutil
# print(psutil.disk_usage('C:'))
# print(psutil.virtual_memory())
# print(psutil.sensors_temperatures())

import random


class LotoCard:
    def __init__(self, player_type):
        self.player_type = player_type
        self._card = [
            [],
            [],
            []
        ]
        self._MAX_NUMBER = 90
        self._MAX_NUMBER_IN_CARD = 15
        self._numbers_stroked = 0
        NEED_SPACES = 4
        NEED_NUMBERS = 5
        self._numbers = random.sample(range(1, self._MAX_NUMBER), self._MAX_NUMBER_IN_CARD)

        for line in self._card:
            for _ in range(NEED_SPACES):
                line.append(' ')
            for _ in range(NEED_NUMBERS):
                line.append(self._numbers.pop())

        # [' ', ' ', ' ', ' ', 10, 5, 9, 7, 6]


        def check_sort_item(item):
            if isinstance(item, int):
                return item
            else:
                return random.randint(1, self._MAX_NUMBER)

        for index, line in enumerate(self._card):
            self._card[index] = sorted(line, key=check_sort_item)


    class LotoGame:
        # player, computer
        pass

human = LotoCard('Ivan')
computer = LotoCard('R2D2')
    #
    # game = LotoGame(human, computer)
    # game.start()
