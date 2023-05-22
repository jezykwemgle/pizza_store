from src.repositor.repository import PizzaRepository
from src.helpers.exeptions import MyException


class PizzaService:

    def __init__(self):
        self.__repository = PizzaRepository()

    def get_all_pizzas(self):
        return self.__repository.get_all_pizzas()

    def get_pizza_by_id(self, choice):
        try:
            if type(choice) == int:
                choice = int(choice)
                result = self.__repository.get_by_id(choice)
                if result is not None:
                    return result[0]
                elif result is None:
                    raise MyException('Wrong id. Please try again')
            else:
                raise MyException('Wrong id. Please try again')
        except MyException as e:
            print(e)

    def lower_price(self, price):
        pizzas = self.__repository.get_all_pizzas()
        try:
            if type(price) == int:
                return [pizza for pizza in pizzas if int(pizza['price']) <= price]
            else:
                raise MyException('Wrong price. Please try again')
        except MyException as e:
            print(e)
            return None

    def pizza_category(self, category):
        pizzas = self.__repository.get_all_pizzas()
        return [pizza for pizza in pizzas if pizza['category'] == category]


if __name__ == '__main__':
    s = PizzaService()
    print(s.get_pizza_by_id(10))
    for i in s.lower_price(150):
        print(i)
    for i in s.pizza_category('classic'):
        print(i)
