__author__ = 'Дмитрий Назаркин'

# == Лото ==
# Правила игры в лото.
# Игра ведется с помощью специальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
#
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
#
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
#
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
#
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
#     Если цифра есть на карточке - она зачеркивается и игра продолжается.
#     Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
#     Если цифра есть на карточке - игрок проигрывает и игра завершается.
#     Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
# Пример одного хода:
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 87     - 14    11
#       16 49    55 88    77
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
#
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.

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
        NEED_SPACES = 4  # пустые клетки
        NEED_NUMBERS = 5  # занятые клиетки
        self._numbers = random.sample(range(1, self._MAX_NUMBER + 1), self._MAX_NUMBER_IN_CARD)
        # [50, 20, 18, 24, 4, 79, 59, 83, 69, 87, 36, 82, 66, 10, 16]

        for line in self._card:
            for _ in range(NEED_SPACES):
                line.append(' ')
            for _ in range(NEED_NUMBERS):
                line.append(self._numbers.pop())

        #  [[' ', ' ', ' ', ' ', 42, 87, 46, 79, 45], [' ', ' ', ' ', ' ', 75, 8, 16, 35, 33], [' ', ' ', ' ', ' ', 49, 58, 30, 72, 61]]

        def check_sort_item(item):
            if isinstance(item, int):
                return item
            else:
                return random.randint(1, self._MAX_NUMBER)

        for index, line in enumerate(self._card):
            self._card[index] = sorted(line, key=check_sort_item)

    @property
    def get_remainder(self):
        count = 0
        for line in self._card:
            count += sum(True for number in line if str(number).isdigit())
        return count

    @property
    def get_card(self):
        MAX_WIDTH_CARD = 42

        def format_item(item):
            item = str(item)
            item = item if len(item) == 2 else f' {item}'
            return item

        border_width_l = (MAX_WIDTH_CARD - len(self.player_type) - 2) // 2
        border_width_r = border_width_l if len(self.player_type) % 2 == 0 else border_width_l + 1

        card = f'{"-" * border_width_l} {self.player_type} {"-" * border_width_r}\n'

        for line in self._card:
            card += ' | '.join(map(format_item, line)) + '\n'
        card += '-' * MAX_WIDTH_CARD

        return card

    def cross_out(self, number):
        count = 0
        for line in self._card:
            if number in line:
                # print(number, line, line.index(number))
                line[line.index(number)] = ' -'
                count += 1

        return count


class LotoGame:
    # player, computer
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer
        self._MAX_NUMBER = 90
        self._rand_list = [x for x in range(1, self._MAX_NUMBER + 1)]
        random.shuffle(self._rand_list)
        # print(len(self._rand_list),self._rand_list)

    def start(self):
        print('Добро пожаловать в игру "Лото"!\n\nПравила:')
        print(f'- всего в игре {self._MAX_NUMBER} ходов\n- вы играете за карточку "{self._player.player_type}"')
        print('- если выпало ваше число - зачеркивайте!\n- при любой ошибке игра заканчивается')
        print('Побеждает тот, кто первый зачеркнет всю карточку.\n!!НАЧИНАЕМ!!\n')

        for turn in range(1, self._MAX_NUMBER + 1):
            current_number = self._rand_list.pop()
            print(f'Новый бочонок: {current_number} (осталось {self._MAX_NUMBER - turn})')
            print(self._player.get_card)
            print(self._computer.get_card)

            human_command = input('Зачеркнуть цифру? (y/n): ')

            # зачеркиваем за компьютера, проверка не победил ли он
            self._computer.cross_out(current_number)
            if self._computer.get_remainder == 0:
                print('Компьютер победил!')
                break

            # проверяем за человека (любой ввод кроме "y" означает "n")
            if human_command == 'y':
                if self._player.cross_out(current_number) == 0:
                    print('Нечего зачеркнуть, вы проиграли :(')
                    break

                if self._player.get_remainder == 0:
                    print('Вы победили! Поздравляем!')
                    break

            else:
                if self._player.cross_out(current_number) > 0:
                    print('Нужно было зачеркнуть, вы проиграли :(')

        print('Игра закончена!')


human = LotoCard('Ivan Ivanov')
computer = LotoCard('AI')

game = LotoGame(human, computer)
game.start()

# print(human.cross_out(22))
# print(human.get_remainder)
# print(human.get_card)
