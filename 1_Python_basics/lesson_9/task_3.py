__author__ = 'Дмитрий Назаркин'

# Реализовать базовый класс Worker (работник):
# -определить атрибуты: name, surname, position (должность), income (доход);
# -последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы «оклад» и «премия», например,
# {"wage": wage, "bonus": bonus};
# -создать класс Position (должность) на базе класса Worker;
# -в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
# с учётом премии (get_total_income);
# -проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров

class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 0, "bonus": 0}

    def set_income(self, wage, bonus):
        self._income['wage'] = wage
        self._income['bonus'] = bonus

class Position(Worker):
    def get_full_name(self):
        print(f'Fullname: {self.name} {self.surname}')

    def get_total_income(self):
        print('Total income:', sum(self._income.values()))

pos1 = Position('Ivan', 'Ivanov', 'manager')
pos1.get_full_name()

pos1.set_income(10000, 5000)
pos1.get_total_income()


pos1 = Position('Petr', 'Pertov', 'CEO')
pos1.get_full_name()

pos1.set_income(300000, 99000)
pos1.get_total_income()