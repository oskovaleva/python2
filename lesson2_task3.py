# Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
# Результат выполнения заданий 1 и 2 должен быть идентичным.

class ItemDiscount:
    def __init__(self, name, price):
        self._name = name
        self.__price = price

    def get_name(self):
        return self._name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'Товар: {self.get_name()}, цена: {self.get_price()}'


item1 = ItemDiscount('item1', 100)
print(item1.get_name(), item1.get_price())
item2 = ItemDiscountReport('item2', 1000)
print(item2.get_parent_data())
