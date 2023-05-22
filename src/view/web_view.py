from src.service .service import PizzaService
from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/')
def main_paige():
    return f"""
        <a href="{url_for('full_menu')}">Full menu</a><br>
        <a href="{url_for('filtering')}">Filtering</a><br>
    """


@app.route('/full-menu/')
def full_menu():
    serv = PizzaService()
    pizzas = []
    for item in serv.get_all_pizzas():
        pizzas.append(str(item))
    return '<br>'.join(pizzas)


@app.route('/filtering/')
def filtering():
    return f"""
        <a href="{url_for('id_filter', id_pizza=1)}">Filtering by id</a><br>
        <a href="{url_for('price_filter', limit=100)}">Filtering by price</a><br>
        <a href="{url_for('category_filter', category='classic')}">Filtering by category</a><br>
    """


@app.route('/id/<id_pizza>')
def id_filter(id_pizza=1):
    serv = PizzaService()
    pizza = serv.get_pizza_by_id(id_pizza)
    return f'{pizza.name} {pizza.price} hrn<br>{pizza.category}: {pizza.ingredients}'


@app.route('/price/<limit>')
def price_filter(limit=0):
    serv = PizzaService()
    pizzas = []
    for item in serv.lower_price(limit):
        pizzas.append(str(item))
    return '<br>'.join(pizzas)


@app.route('/category/<category>')
def category_filter(category='classic'):
    serv = PizzaService()
    pizzas = []
    for item in serv.pizza_category(category):
        pizzas.append(str(item))
    return '<br>'.join(pizzas)


if __name__ == '__main__':
    app.run(debug=True)
