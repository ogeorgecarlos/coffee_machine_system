from classes import Coffee_machine
from functions import header

machine1 = Coffee_machine()

while True:
    header('ā Make your choice:')

    user_choice = input(
        "What would you like? (espresso/latte/cappuccino): \n\nā ").strip().lower()

    if user_choice == 'espresso':
        print(machine1.espresso())
    elif user_choice == 'latte':
        print(machine1.latte())
    elif user_choice == 'cappuccino':
        print(machine1.cappuccino())
    elif user_choice == 'off':
        machine1.off()
    elif user_choice == 'report':
        header('š Report')
        machine1.report()
    else:
        print('ā Enter with a valid option.')

        
