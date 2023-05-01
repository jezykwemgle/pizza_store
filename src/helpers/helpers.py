# для роботи з json
# треба прочитати як працювати з файлами
# продумати як краще: ініціалізувати при створені об'єкта меню чи одразу в кожному методі працювати з джейсоном'

lst = [
    (1, 'Margarita', 100, 'Tomato + cheese', 'vegetarian'),
    (2, 'Vege', 170, 'Tomato + Vege cheese + Paprica', 'vegetarian'),
    (3, 'Pizza Classic', 160, 'Tomato + Ham + Cheese + Parsley', 'classic'),
    (4, 'Meat boom', 200, 'Salami + Ham + Bacon + Veal sous vide + Mozzarella cheese + Onions', 'classic'),
    (5, 'Pepperoni', 180, 'Pepperoni + Mozzarella Cheese + Chili pepper', 'classic'),
    (6, 'Lorenz', 160, 'Veal sous vide + Chicken sous-vide + Mozzarella cheese + Olives + Champions + '
                            'Sweet pepper', 'classic'),
    (7, 'Nautical', 205, 'Cocktail shrimps + Squid + Mussels + Octopus + Mozzarella cheese + Cream',
          'fishy'),
    (8, 'Alpine', 190, 'Smoked chicken + Mozzarella cheese + Champions + Parsley', 'classic'),
    (9, 'El Toro', 200, 'Veal sous vide + Mozzarella cheese + Champions + Sun-dried tomatoes + '
                             'Blue onions', 'classic'),
    (10, 'Vegan Bolognese pizza', 180, 'Vegetable Meat Eat Me At + Thyme + Tomatoes + Garlic + Onions', 'vegan')
]




import csv
from repositor.pizza import Pizza

def print_pizzas(pizzas):
    for pizza in pizzas:
        print(pizza)

def set_data_csv(name, lst):
    with open(name, 'w', newline='') as file:
        wr = csv.writer(file, delimiter=',', quotechar='"')
        wr.writerows(lst)

def get_data_csv(file_name):
    lst = []
    with open(file_name, newline='') as file:
        rd = csv.reader(file, delimiter=',', quotechar='"')
        for row in rd:
            pizza = Pizza(row[0], row[1], row[2], row[3], row[4])
            lst.append(pizza)
    return lst

print_pizzas(get_data_csv('pizzas.csv'))




