class Pizza:
    def __init__(self, pizza_id, name, price, ingredients, category):
        self.__pizza_id = pizza_id
        self.__name = name
        self.__price = price
        self.__ingredients = ingredients
        self.__category = category

    @property
    def pizza_id(self):
        return self.__pizza_id

    @pizza_id.setter
    def pizza_id(self, new_pizza_id):
        self.__pizza_id = new_pizza_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price


    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, new_ingredients):
        self.__ingredients = new_ingredients

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, new_category):
        self.__category = new_category

    def __str__(self):
        return f'Pizza(id: {self.pizza_id}, name: {self.name}, price: {self.price}, ingredients: {self.ingredients}, ' \
               f'category: {self.category})'



