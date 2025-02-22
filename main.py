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
# TODO: 1 Print Prompt at startup
print("Welcome to the Coffee Machine")

#TODO: 6 Provide user menu:  Turn Off, Resource Report, Order Drink

def coffee_machine():
        print("What would you like?")
        print("1. Turn off Coffee Machine")
        print("2. Resource Report")
        print("3. Make Coffee")
        print("4. Exit")
        choice = input("Enter 1, 2, 3, or 4: ")
        if choice == "1":
            return False
        elif choice == "2":
            print_report()
            return True
        elif choice == "3":
            return take_order()
        elif choice == "4":
            return False

# TODO: 2 Turn Machine off

# TODO: 3 Print Resource Report
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print("--------------------------------")
    print("Money: $0.00")
    print("--------------------------------")

# TODO: 4 Take order, confirm resources are sufficient against recipe in menu
def take_order():
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        return False
    elif order == "report":
        print_report()
        return True
    else:
        drink = MENU[order]
        print("+++++++++")
        print(order)
        print("+++++++++")
        for item in drink["ingredients"]:
            if resources[item] < drink["ingredients"][item]:
                print(f"Sorry there is not enough {item}.")
                return True
            else:
                #print cost of drink
                print(f"Price for selected {drink} is: ${drink['cost']}.")
                if process_payment(drink['cost']):
                    resources[item] -= drink["ingredients"][item]
                    print(f"Here is your {order}, enjoy!")
                    print("\n" * 10)
                    return True


# TODO: 5 Process coins, determine payment sufficiency, refund if insufficient, give change if excess, add to bank

def process_payment(price):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if total < price:
        print("Sorry insufficient payment")
        #return money
        return False
    elif total > price:
        print(f"Here is ${total - price} in change.")
        return True
    else:
        print(f"Thank you for your payment.")
        return True


while True:
    coffee_machine()


