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
            print('Wrong answer, please try again')
            self.choice_id(listt)

    def choices(self, listt):
        choice = input('Enter "y" for Yes if you want to see a full menu or "n" for Next: ')
        if choice == 'y':
            for i in listt:
                i = list(i)
                print(f'----------\nName: {i[1]}\nPrice: {i[2]}\nIng: {i[3]}')
        elif choice == 'n':
            try:
                self.choice_id(listt)
            except MyException as e:
                print(f'Catch an error: {e}')
                self.choice_id(listt)
        elif (choice != 'n' or choice != 'y') and type(choice) == str:
            raise MyException('Wrong answer, please try again')

    def lower_price(self, listt, price):
        """
        задача: відсортувати піци за ціною
        користувач вводить ціну, і треба вивести всі піци, що менше за цю ціну
        :return: список кортежів з піцами
        """
        return [pizza for pizza in listt if pizza[2] <= price]

    def pizza_category(self, listt, category):
        """
        задача: відсортувати піци за категорією
        користувач вводить категорію, і треба вивести всі піци за цією категорією
        :return: список кортежів з піцами
        """
        return [pizza for pizza in listt if pizza[4] == category]
