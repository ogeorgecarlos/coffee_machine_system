from prettytable import PrettyTable


class Ingredients:
    def __init__(self):

        self.ingredients = {
            'water': {
                'qtd': 300,
                'unit': 'ml'
            },
            'milk': {
                'qtd': 200,
                'unit': 'ml'
            },
            'coffee': {
                'qtd': 100,
                'unit': 'gr'
            },
        }

    def report_resources(self):
        '''Create a table describe of all items into storage'''

        # Format the storage's info in a table
        self.my_report = PrettyTable()
        self.my_report.add_column("Items", [k for k in self.ingredients])
        self.my_report.add_column("Qtd", [item['qtd'] for item in self.ingredients.values()])
        self.my_report.add_column("Unit", [item['unit'] for item in self.ingredients.values()])
        self.my_report.add_autoindex()

        # returns the table
        return self.my_report

    def add_exist_ingredient(self):
        '''Include more volumn of a existent item '''
        name = self._name_checker("✅ What's the ingredient do you want to add vol?\n\n✔ ")
        vol = self._vol_checker("\n✅ How many vol do you want to add more?\n\n✔ ")
        self.ingredients[name]['qtd'] += float(vol)

    def sub_exist_ingredient(self):
        '''Subtract volumn of a existent item '''

        # Check which item
        name = self._name_checker("✅ What's the ingredient do you want to subtract vol?\n\n✔ ")

        # Check the value to subtract
        while True:
            vol = self._vol_checker("\n✅ How many vol do you want to subtract vol?\n\n✔ ")

            # checks if there is suficient ingredient to subtract
            if self.ingredients[name]['qtd'] - float(vol) < 0:
                print(f"❌ You can't subtract this value, cause this item just had {self.ingredients[name]['qtd']}{self.ingredients[name]['unit']} in the storage.")
            else:
                self.ingredients[name]['qtd'] -= float(vol)
                break

    def clear_ingredients(self):
        '''Clear all volumns of the items in the storage'''
        for item in self.ingredients.values():
            item['qtd'] = 0

    def add_new_ingredient(self):
        '''Add a new ingredient in the storage'''

        # Get the ingredient's name
        choice = 'y'
        while choice == 'y':
            name = input("✅ Enter the new ingredient's name:\n\n✔ ")

            # Checks if the item already exist into storage
            if name in self.ingredients or name == '':
                print('❌ Already exists this item in the list.')

                # ask ifthe user wants to continue with other item
                choice = input("✅ Do you want to enter other ingredient? 'Y' or 'N':\n\n✔ ").strip().lower()
                if choice == 'n':
                    return print("❌ No ingredients added.")
                elif choice not in 'yn' or choice == '':
                    print('❌ Enter a valid option.')
            else:
                break
        
        # get the new ingredient's value
        vol = self._vol_checker("\n✅ How many vol do you want to add to the vol?\n\n✔ ")

        # get the unit for this new item
        unit = input("\n✅ How's the unit do you want to assign to this item? (ml, gr, cm..):\n\n✔  ")

        # adding the new ingredient
        new_ingredient = {name: {'qtd': vol, 'unit': unit}}
        self.ingredients.update(new_ingredient.copy())

    def exclude_ingredient(self):
        '''Add a ingredient in the storage'''
        name = self._name_checker('✅ Type the name of the object that you want to delete.\n\n✔')
        self.ingredients.pop(name)

    def _name_checker(self, text, cond=False):
        '''Checks if the item really is into storage'''
        while True:
            name = input(text).strip().lower()
            # Checks if the item really is into storage
            if name == '':
                print('❌ You need to enter a name')
            elif name in self.ingredients:
                break
            else:
                print(f'❌ There is not "{name}" into the ingredients')
        return name

    def _vol_checker(self, text):
        '''Checks if the vol inputed is valid.'''
        while True:
            vol = input(text).strip().lower()
            # Checks if the item really is into storage and the vol inputed is valid.
            if ',' in vol:
                vol = vol.replace(',', '.')
            if vol == '':
                vol = 0
                break

            try:
                float(vol)
                break
            except:
                print('❌ Enter a valid volumn to increase.')
        return float(vol)


# to test
if __name__ == __name__:
    my_ing = Ingredients()
    print(my_ing.report_resources())
    print()
    my_ing.clear_ingredients()
    print()
    print(my_ing.report_resources())
    print()
    my_ing.add_exist_ingredient()
    print()
    print(my_ing.report_resources())
    my_ing.sub_exist_ingredient()
    print()
    print(my_ing.report_resources())
    my_ing.exclude_ingredient()
    print()
    print(my_ing.report_resources())
    my_ing.add_new_ingredient()
    print()
    print(my_ing.report_resources())


# se ja houver o item na lista perguntar se quer adicionar apenas o volume

#