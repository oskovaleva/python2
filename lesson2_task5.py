# Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний класс.
# Выполнить перегрузку методов конструктора дочернего класса (метод init, в который должна передаваться переменная —
# скидка), и перегрузку метода str дочернего класса. В этом методе должна пересчитываться цена и возвращаться результат
# — цена товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы.

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
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount  # скидка в процентах (от 0 до 100)

    def __str__(self):
        return f'Цена товара {self.get_name()} со скидкой: {self.get_price() * (1 - self.discount / 100):.2f}'

    def get_parent_data(self):
        return f'Товар: {self.get_name()}, цена: {self.get_price()}'


item1 = ItemDiscount('item1', 100)
print(item1.get_name(), item1.get_price())
item2 = ItemDiscountReport('item2', 1000, 10)
print(item2.get_parent_data())
print(item2)
