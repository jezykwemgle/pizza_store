from pizza_repository import PizzaRepository

class PizzaService:

    def __init__(self):
        self.__repository = PizzaRepository()

    def get_pizza_by_id(self, pizza_id):
        return self.__repository.get_by_id(pizza_id)

    def lower_price(self, price):
        pizzas = self.__repository.get_all_pizzas()
        return [pizza for pizza in pizzas if pizza.price <= price]

    def pizza_category(self, category):
        pizzas = self.__repository.get_all_pizzas()
        return [pizza for pizza in pizzas if pizza.category == category]
