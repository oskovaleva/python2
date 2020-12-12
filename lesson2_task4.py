# Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский, и дочерний классы
# получили новое значение цены. Следует проверить это, вызвав соответствующий метод родительского класса и функцию
# дочернего (функция, отвечающая за отображение информации о товаре в одной строке).

class ItemDiscount:
    def __init__(self, name, price):
        self._name = name
        self.__price = price

    def get_name(self):
        return self._name

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'Товар: {self.get_name()}, цена: {self.get_price()}'


item1 = ItemDiscount('item1', 100)
print(item1.get_name(), item1.get_price())
item2 = ItemDiscountReport('item2', 1000)
print(item2.get_parent_data())
item2.set_price(900)
print(item2.get_parent_data())
