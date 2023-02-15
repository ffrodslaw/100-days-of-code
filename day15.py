# Day 15: Coffee machine

######################

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def print_report():
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def count_coins(q, d, n, p):
    total = q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01
    return total


######################

# TODO: 1. Prompt user

# TODO 2: Turn off machine by entering "off"

# TODO 3: Print report of all coffee machine resources.

# TODO: 4. Check resources are sufficient to make drink order.

# TODO: 5. Process coins

# TODO 6. Check if transaction was successful

# TODO 7: Make coffee

machine_on = True

while machine_on:

    drink_choice = input("What would you like (espresso/latte/cappuccino)? ")

    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    if drink_choice == "off":
        machine_on = False
        print("Goodbye")
    elif drink_choice == "report":
        print_report()
    else:
        price = MENU[drink_choice]["cost"]
        needed_resources = MENU[drink_choice]["ingredients"]
        for key in needed_resources:
            if resources[key] < needed_resources[key]:
                print(f"Sorry, there is not enough {key}.")
                machine_on = False
        if machine_on:
            print("Please insert coins.")
            quarters = int(input("How many quarters: "))
            dimes = int(input("How many dimes: "))
            nickels = int(input("How many nickels: "))
            pennies = int(input("How many pennies: "))
            inserted_coins = count_coins(quarters, dimes, nickels, pennies)
            if inserted_coins < price:
                print("Sorry, that's not enough money. Money refunded.")
                machine_on = False
            else:
                resources["water"] -= water
                resources["milk"] -= milk
                resources["coffee"] -= coffee
                if inserted_coins > price:
                    return_coins = -(round(price - inserted_coins, 2))
                    print(f"Here is ${return_coins} in change.")
                money += price
                print(f"Here is your {drink_choice}. Enjoy!")


