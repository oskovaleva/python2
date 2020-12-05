# Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации (нуль необходимо
# исключить). Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону:
# “elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.

import random


def get_random_number(min_num, max_num, length=10):
    if max_num < min_num:
        return 'Incorrect arguments'

    nums_lst = []
    nums_dct = {}
    for i in range(length):
        num = random.randint(max(min_num, 1), max_num)
        nums_lst.append(num)
        nums_dct[f'elem_{num}'] = num
    return nums_lst, nums_dct
