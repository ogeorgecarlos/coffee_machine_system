from sys import exit

from functions import (header, ingredients_checker, ingredients_user,
                       payment_calculate, validate_number)
from requirements import MENU, money, resources


class Coffee_machine:
    def __init__(self):
        self.water = resources['water']
        self.milk = resources['milk']
        self.coffee = resources['coffee']
        self.total_money = 0
        self.money_received = 0
        self.quarters = 0
        self.dimes = 0
        self.nickles = 0
        self.pennies = 0

    def report(self):
        print(f'''
Water : {self.water}ml
Milk: {self.milk}ml
Coffe: {self.coffee}g
Money: $ {self.total_money:.2f}
        ''')

    def off(self):
        header('Encerrando...')
        exit()

    def espresso(self):

        # checkin the ingredients
        ingredients_enough = ingredients_checker(self, 'espresso', MENU)

        if ingredients_enough is False:
            return ''

        # get the payment
        payment = self.get_payment()

        # checking the payment
        calculate_is_ok = payment_calculate(payment, MENU, 'espresso')

        if calculate_is_ok == 'ok':
            ...
        elif calculate_is_ok == 'less':
            self.total_money -= payment
            return '✔ Please, try again.'
        else:
            self.total_money -= calculate_is_ok

        # Preparin the order
        ingredients_user(self, 'espresso', MENU)

        return '☕ Making espresso'

    def latte(self):

        # checkin the ingredients
        ingredients_enough = ingredients_checker(self, 'latte', MENU)

        if ingredients_enough is False:
            return ''

        # get the payment
        payment = self.get_payment()

        # checking the payment
        calculate_is_ok = payment_calculate(payment, MENU, 'latte')

        if calculate_is_ok == 'ok':
            ...
        elif calculate_is_ok == 'less':
            self.total_money -= payment
            return '✔ Please, try again.'
        else:
            self.total_money -= calculate_is_ok

        # Preparin the order
        ingredients_user(self, 'latte', MENU)

        return '☕ Making latte'

    def cappuccino(self):

        # checkin the ingredients
        ingredients_enough = ingredients_checker(self, 'cappuccino', MENU)

        if ingredients_enough is False:
            return ''

        # get the payment
        payment = self.get_payment()

        # checking the payment
        calculate_is_ok = payment_calculate(payment, MENU, 'cappuccino')

        if calculate_is_ok == 'ok':
            ...
        elif calculate_is_ok == 'less':
            self.total_money -= payment
            return '✔ Please, try again.'
        else:
            self.total_money -= calculate_is_ok

        # Preparin the order
        ingredients_user(self, 'cappuccino', MENU)

        return '☕ Making cappuccino'

    def get_payment(self):
        self.money_received = 0
        self.quarters = 0
        self.dimes = 0
        self.nickles = 0
        self.pennies = 0

        header("💷 Payment")

        quarters = validate_number('How many quarters ($0,25)?: ')
        dimes = validate_number('How many dimes ($0,10)?: ')
        nickles = validate_number('How many nickles ($0,05)?: ')
        pennies = validate_number('How many pennies ($0,01)?: ')
        print()

        self.quarters += quarters*money['quarters']
        self.dimes += dimes*money['dimes']
        self.nickles += nickles*money['nickles']
        self.pennies += pennies*money['pennies']

        self.money_received = self.quarters + self.dimes + self.nickles + self.pennies

        self.total_money += self.money_received

        return self.money_received
