# Проверить механизм наследования в Python. Для этого создать два класса.
# Первый — родительский (ItemDiscount), должен содержать статическую информацию о товаре: название и цену.
# Второй — дочерний (ItemDiscountReport), должен содержать функцию (get_parent_data), отвечающую за отображение
# информации о товаре в одной строке. Проверить работу программы.

class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'Товар: {self.name}, цена: {self.price}'


item1 = ItemDiscount('item1', 100)
print(item1.name, item1.price)
item2 = ItemDiscountReport('item2', 1000)
print(item2.get_parent_data())
