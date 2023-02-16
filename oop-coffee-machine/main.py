from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
money = MoneyMachine()
menu = Menu()
menu_item = MenuItem()

is.on = True

while is.on:
    options = menu.get_items()
    order = input(f"What would you like to drink? {options}")
    if order == "report":
        coffee.report()
        money.report()
    elif order == "off":
        is.on = False
    else:
        drink = menu.find_drink(order)
        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee.make_coffee(drink)
