from src.repositor.pizza import Pizza
from src.helpers.helpers import get_data_from_json, set_data_to_json


class PizzaRepository:

    """
    Gets all data with get_data_from_json from json
    """
    @staticmethod
    def get_all_pizzas():
        return get_data_from_json('/home/jezyk_we_mgle/PycharmProjects/pizza_store/src/repositor/pizzas.json')

    """
    Returns new id for item
    """
    def __get_new_id(self):
        pizzas = self.get_all_pizzas()
        return int(pizzas[-1]['id']) + 1 if (len(pizzas) > 0) else 1

    """
    Gets item by id
    """
    def get_by_id(self, pizza_id):
        pizzas = self.get_all_pizzas()
        for pizza in pizzas:
            if int(pizza['id']) == pizza_id:
                # returns tuple (pizza, index)
                return pizza, pizzas.index(pizza)
        return None

    """
    Adds new item to json-file
    """
    def add_pizza(self, pizza: Pizza):
        pizzas = self.get_all_pizzas()
        pizza.pizza_id = self.__get_new_id()
        pizzas.append({'id': pizza.pizza_id, 'name': pizza.name, 'price': pizza.price, 'ingredients': pizza.ingredients, 'category': pizza.category})
        set_data_to_json('/home/jezyk_we_mgle/PycharmProjects/pizza_store/src/repositor/pizzas.json', pizzas)
        return pizza

    """
    Deletes item from json-file
    """
    def delete_pizza(self, pizza_id):
        try:
            pizzas = self.get_all_pizzas()
            pizza = self.get_by_id(pizza_id)[1]
            pizzas.pop(pizza)
            set_data_to_json('/home/jezyk_we_mgle/PycharmProjects/pizza_store/src/repositor/pizzas.json', pizzas)
        except TypeError:
            return None

# todo реалізувати метод оновлення піци
    # def update_pizza(self, pizza_id, new_pizza: Pizza):
    #     pizza = self.get_by_id(pizza_id)
    #     if pizza is None:
    #         raise MyException("Дорогий, ти шо задумав, такої піци не існує")
    #     if type(new_pizza) is Pizza:
    #         pizza.name = new_pizza.name
    #         pizza.price = new_pizza.price
    #         pizza.ingredients = new_pizza.ingredients
    #         pizza.category = new_pizza.category
    #         return pizza
    #     else:
    #         return None


if __name__ == '__main__':
    ...



