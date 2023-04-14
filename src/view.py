from service import PizzaService

service = PizzaService()
pizzas = service.lower_price(160)

for pizza in pizzas:
    print(pizza)
