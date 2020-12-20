# Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она отвечает сообщением,
# целое оно или дробное. Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
# Если они совпадают, программа должна возвращать значение True, иначе False.

import re

user_input = input('Input a number >>> ')

if re.match('^-?[0-9]+$', user_input) is None:
    if re.match('^-?[0-9]+.[0-9]+$', user_input) is None:
        print(f'Your input is not a number')
    else:
        print(f'Number {user_input} is a fractional number')

        sign = 1 if re.match('^-', user_input) is None else -1

        if int(user_input.split('.')[0]) * sign == int(user_input.split('.')[1]):
            print('Fractional part and absolute value of integer part are the same')
        else:
            print('Fractional part and absolute value of integer part are different')

else:
    print(f'Number {user_input} is integer')
