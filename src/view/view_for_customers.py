from service.service import PizzaService

service = PizzaService()
print('Hello, darling! Welcome to our pizza store!')
commands = ['f - Full Menu', 'id - Choose by id', 'fp - Filtering by price', 'fc - Filtering by category',
            'c - See commands', 'Enter - to exit']
print(*commands, sep='\n')
while True:
    print('*******************************')
    choice = input('Please choose the option:')
    if choice == 'f':
        service.print_pizzas(service.get_all_pizzas())
    elif choice == 'id':
        service.get_pizza_by_id()
    elif choice == 'fp':
        service.print_pizzas(service.lower_price())
    elif choice == 'fc':
        service.print_pizzas(service.pizza_category())
    elif choice == 'c':
        print(*commands, sep='\n')
    elif choice == '':
        break
    else:
        print('Something went wrong. Please try again')

