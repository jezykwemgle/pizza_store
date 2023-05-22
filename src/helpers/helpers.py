import json

def print_pizzas(pizzas):
    for pizza in pizzas:
        print(pizza)


# def set_data_csv(name, lst):
#     with open(name, 'w', newline='') as file:
#         wr = csv.writer(file, delimiter=',', quotechar='"')
#         wr.writerows(lst)


# def get_data_csv(file_name):
#     lst = []
#     with open(file_name, newline='') as file:
#         rd = csv.reader(file, delimiter=',', quotechar='"')
#         for row in rd:
#             pizza = Pizza(row[0], row[1], row[2], row[3], row[4])
#             lst.append(pizza)
#     return lst


# def from_class_to_list(list_cl):
#     pizzas = []
#     for item in list_cl:
#         pizzas.append([int(item['id']), item['name'], int(item['price']), item['ingredients'], item['category']])
#     return pizzas


def get_data_from_json(file_name):
    with open(file_name, 'r') as json_file:
        return json.loads(json_file.read())['Pizzas']


def set_data_to_json(file_name, data):
    with open(file_name, 'w') as json_file:
        json.dump({'Pizzas': data}, json_file, indent=4)


if __name__ == '__main__':
    ...
