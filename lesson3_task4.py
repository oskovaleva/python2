# Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл.
# Если файл с таким именем уже существует, выводим соответствующее сообщение.
#
# Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией. Например:
# [91, 42, 47, 64, 60, 23, 82, 78, 22, 15]
# ['zmsebjvdgi', 'ychpwljtzn', 'zqywoopbwf', 'nkxdnnqyhe', 'eqpbrjwjdp',
# 'sllbegvgmh', 'kzrmrozeco', 'jbppumpypu', 'jjsmronkvm', 'qtnspcleqd']
#
# Для создания списков использовать генераторы.
# Применить к спискам функцию zip(). Результат выполнения этой функции должен быть обработан и записан в файл
# таким образом, чтобы каждая строка файла содержала текстовое и числовое значение. Например:
# 91 zmsebjvdgi
# 42 ychpwljtzn
# ...
#
# Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл. Во второй функции необходимо реализовать
# открытие файла и простой построчный вывод содержимого. Вся программа должна запускаться по вызову первой функции.

import os
import random
import string


def print_file_content(path_to_file):
    with open(path_to_file) as f:
        for line in f.readlines():
            print(line, end='')


def create_and_print_file(file_name):
    if os.path.isfile(file_name):
        print('File already exists')
    else:
        numbers = [random.randint(0, 100) for _ in range(10)]
        letters = list(string.ascii_lowercase)
        strings = [''.join([letters[random.randint(0, len(letters) - 1)] for _ in range(10)]) for _ in range(10)]

        with open(file_name, 'w') as f:
            for number, text in zip(numbers, strings):
                print(number, text, file=f)

    print_file_content(file_name)


create_and_print_file('output_task4')
