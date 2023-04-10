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
def choice_id():
    try:
        choice = int(input('Enter id of pizza (1 - 10): '))
        if 1 <= choice <= 10:
            print(
                f'----------\nName: {pizzas[choice - 1][1]}\nPrice: {pizzas[choice - 1][2]}\nIng: {pizzas[choice - 1][3]}')
        elif choice <= 0 or choice >= 11:
            raise MyException('Wrong id')
    except MyException:
        print('Wrong answer, please try again')
        choice_id()
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

def lower_price(pizzas, price):
    """
    задача: відсортувати піци за ціною
    користувач вводить ціну, і треба вивести всі піци, що менше за цю ціну
    :return: список кортежів з піцами
    """
    return [pizza for pizza in pizzas if pizza[2] <= price]

def pizza_category(pizzas, category):
    """
    задача: відсортувати піци за категорією
    користувач вводить категорію, і треба вивести всі піци за цією категорією
    :return: список кортежів з піцами
    """
    return [pizza for pizza in pizzas if pizza[4] == category]


print('Hello, darling! What are you want to eat?\nIf you want to see a menu enter "m".\n'
      'If you want another option, enter"n"')
choice = input(':')
match choice:
    case 'm':
        print('For full menu enter "f"\n For filtering enter "p" for price or "c" for category')
        choice = input(':')
        match choice:
            case 'f':
                for i in pizzas:
                    i = list(i)
                    print(f'----------\nName: {i[1]}\nPrice: {i[2]}\nIng: {i[3]}')
            case 'p':
                price = int(input('Please enter max value:'))
                for i in lower_price(pizzas, price):
                    i = list(i)
                    print(f'----------\nName: {i[1]}\nPrice: {i[2]}\nIng: {i[3]}')
            case 'c':
                category = input('Please enter category (classic, vegan, fishy:')
                for i in pizza_category(pizzas, category):
                    i = list(i)
                    print(f'----------\nName: {i[1]}\nPrice: {i[2]}\nIng: {i[3]}')
    case 'n':
        choice_id()
    case _:
        raise MyException('Wrong answer, please try again')




