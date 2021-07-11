__author__ = 'Дмитрий Назаркин'


# Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка».
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__floordiv____truediv__()). Эти методы должны применяться
# только к клеткам и выполнять увеличение, уменьшение, умножение и округление до целого числа деления клеток соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
# ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Этот метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5.
# В этом случае метод make_order() вернёт строку: *****\n*****\n**.
# Или количество ячеек клетки — 15, а количество ячеек в ряду равняется 5.
# Тогда метод make_order() вернёт строку: *****\n*****\n*****.

class LivingCell:
    def __init__(self, num_cells):
        self.num_cells = num_cells

    def __str__(self):
        return f'В данной клетке {self.num_cells} ячеек'

    def __add__(self, other):
        total_cells = self.num_cells + other.num_cells
        return LivingCell(total_cells)

    def __sub__(self, other):
        total_cells = self.num_cells - other.num_cells
        if total_cells <= 0:
            raise ValueError('Первая клетка меньше второй')
        return LivingCell(total_cells)

    def __mul__(self, other):
        total_cells = self.num_cells * other.num_cells
        return LivingCell(total_cells)

    def __floordiv__(self, other):
        total_cells = self.num_cells // other.num_cells
        return LivingCell(total_cells)

    def __truediv__(self, other):
        total_cells = round(self.num_cells / other.num_cells)
        return LivingCell(total_cells)

    def make_order(self, number):
        cell_str = '*' * self.num_cells
        cell_list = [cell_str[i:i + number] for i in range(0, self.num_cells, number)]
        return '\n'.join(cell_list)


cell_1 = LivingCell(150)
cell_2 = LivingCell(70)

new_cell = cell_1 + cell_2
print(new_cell)
print(new_cell.make_order(50))

new_cell = cell_1 - cell_2
print(new_cell)
print(new_cell.make_order(44))

new_cell = cell_1 * cell_2
print(new_cell)

new_cell = cell_1 // cell_2
print(new_cell)

new_cell = cell_1 / cell_2
print(new_cell)
