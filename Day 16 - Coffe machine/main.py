from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

isOn = True

while isOn:
    want = input(f"What would you like? ({menu.get_items()}): ")
    if want == 'report':
        coffee_maker.report()
        money_machine.report()
    elif want == 'off':
        isOn = False
    else:
        drink = menu.find_drink(want)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
