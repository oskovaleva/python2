# Инкапсулировать оба параметра (название и цену) товара родительского класса.
# Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.

class ItemDiscount:
    def __init__(self, name, price):
        self._name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'Товар: {self._name}, цена: {self._ItemDiscount__price}'


# Сделала два уровня инкапсуляции. Полностью закрыть доступ к переменным в python нельзя.
# В текущем виде программа выполняется, хоть pep8 и ругается на доступ к инкапсулированным переменным.
item1 = ItemDiscount('item1', 100)
print(item1._name, item1._ItemDiscount__price)
item2 = ItemDiscountReport('item2', 1000)
print(item2.get_parent_data())
