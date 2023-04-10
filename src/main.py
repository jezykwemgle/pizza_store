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
print('Hello, darling! What are you want to eat?')
def choice_id():
    choice = int(input('If you already know a menu, enter id of pizza (1 - 10): '))
    if 1 <= choice <= 10:
        print(
            f'----------\nName: {pizzas[choice - 1][1]}\nPrice: {pizzas[choice - 1][2]}\nIng: {pizzas[choice - 1][3]}')
    elif choice <= 0 or choice >= 11:
        raise MyException('Wrong id')
def choices():
    choice = input('Enter "y" for Yes if you want to see a full menu or "n" for Next: ')
    if choice == 'y':
        for i in pizzas:
            i = list(i)
            print(f'----------\nName: {i[1]}\nPrice: {i[2]}\nIng: {i[3]}')
    elif choice == 'n':
        try:
            choice_id()
        except MyException as e:
            print(f'Catch an error: {e}')
            choice_id()
    elif (choice != 'n' or choice != 'y') and type(choice) == str:
        raise MyException('Wrong answer, please try again')
try:
    choices()
except MyException as e:
    print(f'Catch an error: {e}')
    choices()

def lower_price(price):
    """
    задача: відсортувати піци за ціною
    користувач вводить ціну, і треба вивести всі піци, що менше за цю ціну
    :return: список кортежів з піцами
    """

def pizza_category(category):
    """
    задача: відсортувати піци за категорією
    користувач вводить категорію, і треба вивести всі піци за цією категорією
    :return: список кортежів з піцами
    """




