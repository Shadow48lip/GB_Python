__author__ = 'Дмитрий Назаркин'


# a) Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором
# ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
#
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам? Можно ли
# использовать словарь в этом случае?
#
# *(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия»
# и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме
# редыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
# Как поступить, если потребуется сортировка по ключам?

# a)
def thesaurus(*names):
    """Возвращает картотеку сотрудников"""
    first_letters = list(set([letter[0] for letter in names]))
    first_letters.sort()
    catalog = dict()

    for letter in first_letters:
        # Вариант 1  (не ракомендуется вроде как)
        # name_line = list(filter(lambda name: name.startswith(letter), names))
        # catalog[letter] = name_line

        # Вариант 2 через .update
        name_line = {letter: list(filter(lambda name: name.startswith(letter), names))}
        catalog.update(name_line)

    return catalog


print('Вариант а):', thesaurus("Иван", "Мария", "Петр", "Илья"))

# b) под звездочкой
def split_name(name):
    f_name, l_name = name.split()
    return l_name[0]

def thesaurus_adv(*names):
    first_letters = list(set(map(split_name, names)))
    first_letters.sort()
    catalog = dict()

    for letter in first_letters:
        name_list = list(filter(lambda name: name.split()[1].startswith(letter), names))

        second_letters = list(set([letter[0] for letter in name_list]))
        second_letters.sort()

        second_dict = {}
        for letter2 in second_letters:
            name_line = list(filter(lambda name: name.startswith(letter2), name_list))
            line_pair = {letter2: name_line}
            second_dict.update(line_pair)

        catalog.update({letter: second_dict})

    return catalog


print('Вариант b):', thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
