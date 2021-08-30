class Car:
    def __init__(self):
        self.modules = []
        self.fc = 7

    def __call__(self, price=None):
        print(f'Собран автомобиль {self.name} с модулями {self.modules}, цена: {price}')

    def __add__(self, other):
        self.modules.append(other)
        return self

    def __str__(self):
        return f'Авто с модулями: {self.modules}'

    def __setattr__(self, key, value):
        # super().__setattr__(key, value)
        self.__dict__[key] = value
        print(f'создан атрибут {key} со значением {value}')

    def __eq__(self, other):
        return self.fc == other.fc

    def __getitem__(self, item):
        return self.modules[item]

    def __del__(self):
        print('объект удален')


# car1 = Car()
# car2 = Car()
# module1 = 'теплый руль'
# module2 = 'бронированное стекло'
# module3 = 'турель'

# car + module1 + module2 + module3  # car.modules.append(module1)
# car + module2  # car.modules.append(module2)
# car + module3  # car.modules.append(module3)
# car.name = 'Tesla'
# print(car[2].upper())
# car(5000)

# print()
# print(car == car)
# print(car1 == car2)
# car2.fc = 10
# print(car1 == car2)

from abc import ABC, abstractmethod


class MyAbsClass(ABC):
    def __init__(self):
        self.x = 0

    @abstractmethod
    def my_method1(self):
        pass

    @abstractmethod
    def my_method2(self):
        pass


class MyClass(MyAbsClass):
    def my_method1(self):
        print('my_method1')

    def my_method22(self):
        print('my_method1')

    def qwe(self):
        print('qwe')


# mc = MyClass()


# for i in 123:
#     print(i)

class Iterator:
    def __init__(self):
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i <= 7:
            return self.i
        else:
            raise StopIteration


#
# qwe = Iterator()
# for i in qwe:
#     print(i)


class Human:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        # check age
        if self._age > 100 or self._age < 0:
            return -1
        return self._age


# code
# human = Human('Ivan', -5)
# print(human.age)

class WinDoor:
    def __init__(self, w, h):
        self.square = w * h


class Room:
    def __init__(self, l1, l2, h):
        self.square = 2 * h * (l1 + l2)
        self.wd = []

    def add_windoor(self, w, h):
        self.wd.append(WinDoor(w, h))

    def common_square(self):
        for el in self.wd:
            self.square -= el.square
        return self.square


r = Room(10, 8, 4)
print(r.square)
r.add_windoor(2, 3)
r.add_windoor(3, 3)
r.add_windoor(4, 2)

print(r.common_square())
