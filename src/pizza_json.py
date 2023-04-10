import json
pizzas = {
    (1, 'Margarita', 100, 'Tomato + cheese', 'vegetarian'),
    (2, 'Quarto Formaggi', 190, 'tomato + Mozzarella cheese + Blue cheese, Parmigiana + Gauda', 'vegetarian'),
    (3, 'Pizza Classic', 160, 'Tomato + Ham + Cheese + Parsley', 'classic'),
    (4, 'Meat boom', 200, 'Salami + Ham + Bacon + Veal sous vide + Mozzarella cheese + Onions', 'classic'),
    (5, 'Pepperoni', 180, 'Pepperoni + Mozzarella Cheese + Chili pepper', 'classic'),
    (6, 'Lorenz', 160, 'Veal sous vide + Chicken sous-vide + Mozzarella cheese + Olives + Champions + Sweet pepper',
     'classic'),
    (7, 'Nautical', 205, 'Cocktail shrimps + Squid + Mussels + Octopus + Mozzarella cheese + Cream', 'without meet'),
    (8, 'Alpine', 190, 'Smoked chicken + Mozzarella cheese + Champions + Parsley', 'classic'),
    (8, 'Alpine', 190, 'Smoked chicken + Mozzarella cheese + Champions + Parsley', 'classic'),
    (9, 'El Toro', 200, 'Veal sous vide + Mozzarella cheese + Champions + Sun-dried tomatoes + Blue onions',
     'classic'),
    (10, 'Vegan Bolognese pizza', 180, 'Vegetable Meat Eat Me At+ Thyme + Tomatoes + Garlic + Onions', 'vegan')
}
pizzas_dict = []
for pizza in pizzas:
    pizza_dict = {}
    pizza_dict['id'] = pizza[0]
    pizza_dict['name'] = pizza[1]
    pizza_dict['price'] = pizza[2]
    pizza_dict['ingredients'] = pizza[3]
    pizza_dict['category'] = pizza[4]
    pizzas_dict.append(pizza_dict)

with open('pizzas', 'w') as file:
    json.dump(pizzas_dict, file, indent=4)







