from typing import Tuple, Any


class Pizza:
    def __init__(self, pizza_id, name, price, ingredients, category):
        self.pizza_id = pizza_id
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.category = category

    def __str__(self):
        return f'Pizza(id: {self.pizza_id}, name: {self.name}, price: {self.price}, ingredients: {self.ingredients}, ' \
               f'category: {self.category})'



