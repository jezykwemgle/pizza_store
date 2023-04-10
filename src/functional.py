import json
from exeptions import MyException

class Functional:
    def __init__(self):
        pass

    def read(self, listt):
        for i in listt:
            i = list(i)
            print(f'----------\nName: {i[1]}\nPrice: {i[2]}\nIng: {i[3]}')
    def list_to_json(self, listt):
        pizzas_dict = []
        for pizza in listt:
            pizza_dict = {}
            pizza_dict['id'] = pizza[0]
            pizza_dict['name'] = pizza[1]
            pizza_dict['price'] = pizza[2]
            pizza_dict['ingredients'] = pizza[3]
            pizza_dict['category'] = pizza[4]
            pizzas_dict.append(pizza_dict)

        with open('pizzas', 'w') as file:
            json.dump(pizzas_dict, file, indent=4)

    def choice_id(self, listt):
        try:
            choice = int(input('Enter id of pizza (1 - 10): '))
            if 1 <= choice <= 10:
                print(
                    f'----------\nName: {listt[choice - 1][1]}\nPrice: {listt[choice - 1][2]}\nIng: {listt[choice - 1][3]}')
            elif choice <= 0 or choice >= 11:
                raise MyException('Wrong id')
        except MyException:
            print('Please try again')
            self.choice_id(listt)

    def choices(self, listt):
        try:
            choice = input('For full menu enter "f"\n For filtering enter "p" for price or "c" for category:')
            if choice == 'p':
                price = int(input('Please enter max value:'))
                self.read(self.lower_price(listt, price))
            elif choice == 'c':
                category = input('Please enter category (classic, vegan, fishy:')
                self.read(self.pizza_category(listt, category))
            elif choice == 'f':
                self.read(listt)
            elif (choice != 'p' or choice != 'c' or choice != 'f') and type(choice) == str:
                raise MyException('Wrong answer')
        except MyException:
            print('Please try again')
            self.choices(listt)

    def lower_price(self, listt, price):
        return [pizza for pizza in listt if pizza[2] <= price]

    def pizza_category(self, listt, category):
        return [pizza for pizza in listt if pizza[4] == category]
