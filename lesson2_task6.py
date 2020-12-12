# Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на два класса.
# Инициализировать классы необязательно.
#
# Внутри каждого поместить функцию get_info, которая в первом классе будет отвечать за вывод названия товара,
# а во втором — его цены. Далее реализовать выполнение каждой из функций тремя способами.

from abc import ABC, abstractmethod


class ItemDiscount:
    def __init__(self, name, price):
        self._name = name
        self.__price = price

    def get_name(self):
        return self._name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount, ABC):
    @abstractmethod
    def get_info(self):
        pass


class ItemReport1(ItemDiscountReport):
    def get_info(self):
        return self.get_name()


class ItemReport2(ItemDiscountReport):
    def get_info(self):
        return self.get_price()


item1 = ItemReport1('item1', 100)
print(item1._name)
print(item1.get_name())
print(item1.get_info())

item2 = ItemReport2('item2', 1000)
print(item2._ItemDiscount__price)
print(item2.get_price())
print(item2.get_info())
