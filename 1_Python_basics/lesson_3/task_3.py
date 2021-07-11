__author__ = 'Дмитрий Назаркин'

# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх
# списков (по одному из каждого):
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово
# можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

import random, itertools


def get_jokes(num_jokes, repeat=True):
    """
    Функция генерации случайных шуток
    :param num_jokes: количество шуток
    :param repeat: разрешать ли повторы слов
    :return: list шуток
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    jokes = list()
    # защита от большего числа повторов, чем в списках слов при запрете посторов
    num = len(nouns) if not repeat and num_jokes > len(nouns) else num_jokes

    for num in range(num):
        word_1 = random.choice(nouns)
        word_2 = random.choice(adverbs)
        word_3 = random.choice(adjectives)

        if not repeat:
            nouns.remove(word_1)
            adverbs.remove(word_2)
            adjectives.remove(word_3)

        jokes.append(f'{word_1} {word_2} {word_3}')

    return jokes


print('С повторами',get_jokes(3))
print('Без повторов',get_jokes(6, False))
