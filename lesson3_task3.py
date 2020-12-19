# Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
# Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения, в словаре
# для него должно сохраняться значение None. Значения, которым не хватило ключей, необходимо отбросить.

def dict_maker(keys: list, values: list):
    dct = {}
    for ind in range(len(keys)):
        try:
            dct[keys[ind]] = values[ind]
        except IndexError:
            dct[keys[ind]] = None
    return dct


lst1 = [0, 1, 2, 3]
lst2 = [0, 1, 2, 3, 4, 5]
print(dict_maker(lst1, lst2))
print(dict_maker(lst2, lst1))
