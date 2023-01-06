def header(text):
    print()
    print(40*'-')
    print(f'{text:^40}')
    print(40*'-')
    print()


def payment_calculate(payment, MENU, type):
    if payment < MENU[type]['cost']:
        print(f"❌ You put a total of $ {payment};\n☕ The {type} cost ${MENU[type]['cost']}.\n💲 Your money will be returned.")
        return 'less'
    if payment > MENU[type]['cost']:
        rest = payment - MENU[type]['cost']
        print(f"💷 You put a total of $ {payment:.2f}, but it's cost $ {MENU[type]['cost']:.2f}.\n💲 Then, we will return to you a total of $ {rest:.2f}.\n")
        return rest
    else:
        print('✅ Payment is ok!')
        return 'ok'


def ingredients_checker(self, type, MENU):

    # variables if is espresso or not.
    if type == 'espresso':
        ingredients_enough = self.water - MENU[type]['ingredients']['water'] >= 0 and self.coffee - MENU[type]['ingredients']['coffee'] >= 0
    elif type != 'espresso':
        ingredients_enough = self.water - MENU[type]['ingredients']['water'] > 0 and self.coffee - MENU[type]['ingredients']['coffee'] >= 0 and self.milk - MENU[type]['ingredients']['milk'] >= 0

    # cheking ingredients
    if not ingredients_enough:
        print(f'\n😥 Sorry, there is not enough ingredients to make a {type}.')
        return False
    else:
        return True


def ingredients_user(self, type, MENU):
    if type == 'espresso':
        self.water -= MENU[type]['ingredients']['water']
        self.coffee -= MENU[type]['ingredients']['coffee']
    else:
        self.water -= MENU[type]['ingredients']['water']
        self.coffee -= MENU[type]['ingredients']['coffee']
        self.milk -= MENU[type]['ingredients']['milk']


def validate_number(text):
    while True:
        x = input(f'{text}')
        try:
            if ',' in x:
                x.replace(',', '.')
            float(x)
            break
        except:
            print("❌ Enter with a valid number.")
    return float(x)
