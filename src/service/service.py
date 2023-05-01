from repositor.repository import PizzaRepository
from helpers.exeptions import MyException


class PizzaService:

    def __init__(self):
        self.__repository = PizzaRepository()

    def get_pizza_by_id(self, choice):
        try:
            result = self.__repository.get_by_id(choice)
            if result is not None:
                return result
            elif result is None:
                raise MyException('Wrong id')
        except MyException:
            print('Please try again')
            self.get_pizza_by_id()

    def get_all_pizzas(self):
        return self.__repository.get_all_pizzas()

    # def delete_pizza(self, pizza_id):
    #     pizza = self.__repository.get_by_id(pizza_id)
    #     pizza.isDeleted = True
    #     self.__repository.update_pizza(pizza)

    def lower_price(self):
        pizzas = self.__repository.get_all_pizzas()
        price = int(input('Enter the upper limit:'))
        return [pizza for pizza in pizzas if pizza.price <= price]

    def pizza_category(self):
        pizzas = self.__repository.get_all_pizzas()
        category = input('Enter category. Available are classic, vegetarian, fishy, vegan:')
        return [pizza for pizza in pizzas if pizza.category == category]


if __name__ == '__main__':
    s = PizzaService()
    for i in s.get_all_pizzas():
        print(i)
