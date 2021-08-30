__author__ = 'Дмитрий Назаркин'


# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для
# перевода: какой тип данных выбрать, в теле функции или снаружи.
#
# 2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с
# числительными, начинающимися с заглавной буквы. Например:
# >>> >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

# вариант 1
def num_translate(number):
    """Перевод числительных с eng -> rus"""
    num_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    return num_dict.get(number, None)


print(num_translate('two'))
print(num_translate('four'))
print(num_translate('seven'))
print(num_translate('qwe'))


# вариант 2
def num_translate_adv(number):
    """Перевод числительных с eng -> rus с учетмом заглавной буквы"""
    num_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

    if number[0].isupper():
        # None незльзя капитализить, потому делаем по другому, чтоб не ловить ошибку
        # return num_dict.get(number.lower(), None).capitalize()
        if number.lower() in num_dict:
            return num_dict.get(number.lower()).capitalize()
        else:
            return None
    else:
        return num_dict.get(number, None)


print(num_translate_adv('two'))
print(num_translate_adv('Two'))
print(num_translate_adv('ten'))
print(num_translate_adv('Ten'))
print(num_translate_adv('Qweу'))
