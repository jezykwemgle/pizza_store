import csv
from src.repositor.pizza import Pizza

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

def from_class_to_list(list_cl):
    pizzas = []
    for item in list_cl:
        pizzas.append([int(item.pizza_id), item.name, int(item.price), item.ingredients, item.category])
    return pizzas

if __name__ == '__main__':
    print_pizzas(get_data_csv('../repositor/pizzas.csv'))







