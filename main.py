from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Initialize objects

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

# Start coffee machine
is_on = True


while is_on:
    # Get available items and ask for user choice
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")


    if choice == "off":
        # Turn machine off
        is_on = False
    elif choice == "report":
        # Generate reports for resources and money
        coffee_maker.report()
        money_machine.report()
    else:
        # Handle drink selection
        drink = menu.find_drink(choice)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                print(f"the cost for {drink.name} is {drink.cost}")
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
                    continue
                else:
                    print("Sorry that's not enough money. Money refunded.")
                    print("Sorry there is not enough resources to make that coffee.")
                    print("Money refunded.")
        else:
            print("Invalid input")