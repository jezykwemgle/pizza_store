from helpers.exeptions import MyException
from repositor.pizza import Pizza

class PizzaRepository:

    def __init__(self):
        self.__pizzas = [
            Pizza(1, 'Margarita', 100, 'Tomato + cheese', 'vegetarian'),
            Pizza(2, 'Vege', 170, 'Tomato + Vege cheese + Paprica', 'vegetarian'),
            Pizza(3, 'Pizza Classic', 160, 'Tomato + Ham + Cheese + Parsley', 'classic'),
            Pizza(4, 'Meat boom', 200, 'Salami + Ham + Bacon + Veal sous vide + Mozzarella cheese + Onions', 'classic'),
            Pizza(5, 'Pepperoni', 180, 'Pepperoni + Mozzarella Cheese + Chili pepper', 'classic'),
            Pizza(6, 'Lorenz', 160, 'Veal sous vide + Chicken sous-vide + Mozzarella cheese + Olives + Champions + '
                  'Sweet pepper', 'classic'),
            Pizza(7, 'Nautical', 205, 'Cocktail shrimps + Squid + Mussels + Octopus + Mozzarella cheese + Cream',
                  'fishy'),
            Pizza(8, 'Alpine', 190, 'Smoked chicken + Mozzarella cheese + Champions + Parsley', 'classic'),
            Pizza(9, 'El Toro', 200, 'Veal sous vide + Mozzarella cheese + Champions + Sun-dried tomatoes + '
                  'Blue onions', 'classic'),
            Pizza(10, 'Vegan Bolognese pizza', 180, 'Vegetable Meat Eat Me At + Thyme + Tomatoes + Garlic + Onions',
                  'vegan')
        ]

    def __get_new_id(self):
        return int(self.__pizzas[-1].pizza_id) + 1 if (len(self.__pizzas) > 0) else 1

    def get_all_pizzas(self):
        return self.__pizzas

    def get_by_id(self, pizza_id):
        for pizza in self.__pizzas:
            if pizza.pizza_id == pizza_id:
                return pizza
        return None

    def add_pizza(self, pizza):
        pizza.pizza_id = self.__get_new_id()
        self.__pizzas.append(pizza)
        return pizza

    def delete_pizza(self, pizza_id):
        self.__pizzas.remove(self.get_by_id(pizza_id))

    def update_pizza(self, pizza_id, new_pizza):
        pizza = self.get_by_id(pizza_id)
        if pizza is None:
            raise MyException("Дорогий, ти шо задумав, такої піци не існує")
        if type(new_pizza) is Pizza:
            pizza.name = new_pizza.name
            pizza.price = new_pizza.price
            pizza.ingredients = new_pizza.ingredients
            pizza.category = new_pizza.category
            return pizza
        else:
            return None
if __name__ == '__main__':
    r = PizzaRepository()
    for i in r.get_all_pizzas():
        print(i)