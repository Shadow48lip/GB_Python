__author__ = 'Дмитрий Назаркин'


# Реализуйте базовый класс Car:
# - у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# - опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# - добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# - для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self._show_attr()

    def _show_attr(self):
        is_police = 'Полицеский.' if self.is_police else 'Не относится к полиции.'
        print(f'Автомобиль {self.name}, цвет {self.color}. {is_police}')

    def go(self):
        print(f'Автомобиль {self.name} поехал')

    def stop(self):
        self.speed = 0
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):
        '''Влево - L, вправо - R'''
        direction = 'влево' if direction == 'L' else 'вправо'
        print('Автомобиль повернул:', direction)

    def show_speed(self):
        print(f'Скорость: {self.speed} км.ч.')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Внимание! Ваша скорость {self.speed} выше допустимой 60 км.ч.')
        else:
            print(f'Скорость: {self.speed} км.ч.')



class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Внимание! Ваша скорость {self.speed} выше допустимой 40 км.ч.')
        else:
            print(f'Скорость: {self.speed} км.ч.')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)



c1 = TownCar(100, 'белый', 'Mazda')
c1.show_speed()
c1.speed = 50
c1.show_speed()

c2 = SportCar(160, 'красный', 'Ferrari')
c2.go()
c2.turn('L')

c3 = WorkCar(50, 'белый', 'Газель')
c3.show_speed()
c3.speed = 40
c3.show_speed()

p = PoliceCar(60, 'голубой', 'Opel')
p.show_speed()
p.stop()
p.show_speed()


