from src.helpers.exeptions import MyException
from src.repositor.pizza import Pizza
from src.helpers.helpers import get_data_csv, set_data_csv, from_class_to_list

class PizzaRepository:

    @staticmethod
    def get_all_pizzas():
        pizzas = get_data_csv('../repositor/pizzas.csv')
        return pizzas

    def __get_new_id(self):
        pizzas = self.get_all_pizzas()
        return int(pizzas[-1].pizza_id) + 1 if (len(pizzas) > 0) else 1

    def get_by_id(self, pizza_id):
        pizzas = self.get_all_pizzas()
        for pizza in pizzas:
            if int(pizza.pizza_id) == pizza_id:
                # return tuple (pizza, index)
                return pizza, pizzas.index(pizza)
        return None

    def add_pizza(self, pizza: Pizza):
        pizzas = self.get_all_pizzas()
        pizza.pizza_id = self.__get_new_id()
        pizzas.append(pizza)
        set_data_csv('../repositor/pizzas.csv', from_class_to_list(pizzas))
        return pizza

    def delete_pizza(self, pizza_id):
        try:
            pizzas = self.get_all_pizzas()
            pizza = self.get_by_id(pizza_id)[1]
            pizzas.pop(pizza)
            set_data_csv('../repositor/pizzas.csv', from_class_to_list(pizzas))
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





