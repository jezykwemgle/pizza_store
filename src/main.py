from functional import Functional
from exeptions import MyException
pizzas = [
    (1, 'Margarita', 100, 'Tomato + cheese', 'vegetarian'),
    (2, 'Quarto Formaggi', 190, 'tomato + Mozzarella cheese + Blue cheese, Parmigiano + Gauda', 'vegetarian'),
    (3, 'Pizza Classic', 160, 'Tomato + Ham + Cheese + Parsley', 'classic'),
    (4, 'Meat boom', 200, 'Salami + Ham + Bacon + Veal sous vide + Mozzarella cheese + Onions', 'classic'),
    (5, 'Pepperoni', 180, 'Pepperoni + Mozzarella Cheese + Chili pepper', 'classic'),
    (6, 'Lorenz', 160, 'Veal sous vide + Chicken sous-vide + Mozzarella cheese + Olives + Champions + Sweet pepper',
     'classic'),
    (7, 'Nautical', 205, 'Cocktail shrimps + Squid + Mussels + Octopus + Mozzarella cheese + Cream', 'without meet'),
    (8, 'Alpine', 190, 'Smoked chicken + Mozzarella cheese + Champions + Parsley', 'classic'),
    (9, 'El Toro', 200, 'Veal sous vide + Mozzarella cheese + Champions + Sun-dried tomatoes + Blue onions',
     'classic'),
    (10, 'Vegan Bolognese pizza', 180, 'Vegetable Meat Eat Me At+ Thyme + Tomatoes + Garlic + Onions', 'vegan')
]

f = Functional()
print('Hello, darling! What are you want to eat?\nIf you want to see a menu enter "m".\n' 
      'If you want another option, enter "n":', end='')
choice = input()
try:
    match choice:
        case 'm':
            f.choices(pizzas)
        case 'n':
            f.choice_id(pizzas)
        case _:
            raise MyException('Wrong answer, please try again')
except MyException:
    print('Program is stoped')





