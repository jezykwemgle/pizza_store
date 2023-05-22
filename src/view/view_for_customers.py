from src.service .service import PizzaService
from src.helpers.helpers import print_pizzas

service = PizzaService()
print('Hello, darling! Welcome to our pizza store!')
commands = ['f - Full Menu', 'id - Choose by id', 'fp - Filtering by price', 'fc - Filtering by category',
            'c - See commands', 'Enter - to exit']
print(*commands, sep='\n')
while True:
    print('*******************************')
    choice = input('Please choose the option:')
    if choice == 'f':
        print_pizzas(service.get_all_pizzas())
    elif choice == 'id':
        choice = input('Enter pizza id : ')
        r = service.get_pizza_by_id(choice)
        if r is not None:
            print(service.get_pizza_by_id(choice))
    elif choice == 'fp':
        choice = input('Enter the upper limit:')
        r = service.lower_price(choice)
        if r is not None:
            print_pizzas(r)
    elif choice == 'fc':
        choice = input('Enter category. Available are classic, vegetarian, fishy, vegan:')
        r = service.pizza_category(choice)
        if r is not None:
            print_pizzas(r)
    elif choice == 'c':
        print(*commands, sep='\n')
    elif choice == '':
        break
    else:
        print('Something went wrong. Please try again')

