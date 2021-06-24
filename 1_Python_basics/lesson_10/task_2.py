__author__ = 'Дмитрий Назаркин'

# Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать абстрактные
# классы для основных классов проекта и проверить работу декоратора @property.

from abc import ABC, abstractmethod

class DressAbsClass(ABC):
    def __init__(self):
        self.total = 0

    def __str__(self):
        return f'Общий расход {self.total} м.'

    @abstractmethod
    def calculation(self, size):
        pass


class CalcSuit(DressAbsClass):
    def calculation(self, size):
        consumption = 2 * size + 0.3
        self.total += consumption
        print(f'Раход ткани по костюму {consumption} м.')

class CalcСoat(DressAbsClass):
    def calculation(self, size):
        consumption = round(size/6.5 + 0.5, 1)
        self.total += consumption
        print(f'Раход ткани по пальто {consumption} м.')


class TotalCalc:
    def __init__(self, suit, coat):
        self.suit = suit
        self.coat = coat

    @property
    def get_total(self):
        print('Общий расход такани ',self.suit.total + self.coat.total,'м.')

suit = CalcSuit()
suit.calculation(10)
suit.calculation(5)
suit.calculation(1)
print(suit)

coat = CalcСoat()
coat.calculation(12)
coat.calculation(4)
print(coat)

print()
total = TotalCalc(suit, coat)
total.get_total