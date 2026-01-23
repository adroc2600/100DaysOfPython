from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

while True: 
    selection = input(f"What would you like? ({my_menu.get_items()}): ").lower()
    if selection == "off":
        sys.exit()
    if selection == "report":
        my_coffee_maker.report()
    while selection != "latte" and drink != "espresso" and drink != "cappuccino":
        selection = input(f"What would you like? ({my_menu.get_items()}): ").lower()

    drink = my_menu.find_drink(selection)

    if not my_coffee_maker.is_resource_sufficient(drink):
        sys.exit()
        
    if my_money_machine.make_payment(drink.cost):
        my_coffee_maker.make_coffee(drink)