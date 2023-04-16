from service import PizzaService

service = PizzaService()
pizzas = service.lower_price(170)

for pizza in pizzas:
    print(pizza)

print("\n/////////////////////////////\n")

pizzas = service.pizza_category('vegetarian')

print(service.get_pizza_by_id(7))
for pizza in pizzas:
    print(pizza)
