## AI Assistant
# Coffee Machine Program

This project is a simple simulation of a coffee machine built using Python. The coffee machine provides functionality to serve three types of coffee—**Espresso**, **Latte**, and **Cappuccino**—and interact with users to take orders, process payments, and track machine resources like water, milk, and coffee.

---

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Menu Options](#menu-options)
- [Available Drinks](#available-drinks)
- [Resource Management](#resource-management)
- [Payment System](#payment-system)
- [Future Updates](#future-updates)
- [How to Run](#how-to-run)

---

## Features

1. **Interactive Menu**: Users can choose from several options, such as making a drink, viewing a resource report, or turning the machine off.
2. **Resource Tracking**: Tracks the availability of required ingredients (water, milk, coffee) and ensures sufficient resources before fulfilling an order.
3. **Payment Processing**: Handles coin-based payment, calculates total, checks for sufficient funds, provides change if necessary, and adds collected money to the machine's bank.
4. **Three Drink Recipes**: The machine can prepare Espresso, Latte, or Cappuccino, using predefined recipes and costs.
---

## How It Works

1. The program starts by displaying a welcome message.
2. An interactive menu is presented to the user, where they can:
   - Turn off the machine.
   - View a report of the machine's resources.
   - Order a drink of their choice (Espresso, Latte, or Cappuccino).
3. If a drink is ordered:
   - The machine checks if there are enough resources.
   - If sufficient, it processes coins inserted by the user.
   - It dispenses change if paid in excess and deducts the used resources.
   - If insufficient resources or payment, the program will notify the user.
4. The process repeats until the machine is turned off.

---

## Menu Options

In the main menu, users can choose one of the following options:

- **Turn Off the Coffee Machine**: Exit the program.
- **Resource Report**: View the current supply levels and bank balance.
- **Make Coffee**: Order and prepare one of the three available drinks (Espresso, Latte, Cappuccino).
- **Exit the Program**: Safely close the program without any action.

---

## Available Drinks

The coffee machine can make the following drinks with the specified recipes and costs:

1. **Espresso**
   - **Ingredients**: 50ml water, 18g coffee
   - **Cost**: $1.50
2. **Latte**
   - **Ingredients**: 200ml water, 150ml milk, 24g coffee
   - **Cost**: $2.50
3. **Cappuccino**
   - **Ingredients**: 250ml water, 100ml milk, 24g coffee
   - **Cost**: $3.00

---

## Resource Management

The coffee machine tracks and manages its resources:
- Water
- Milk
- Coffee

The machine checks if there are sufficient resources before preparing a drink. If there aren’t enough resources, the user is notified. The current resource levels can be viewed using the "Resource Report" option in the main menu.

### Initial Machine Resources:

- **Water**: 300ml
- **Milk**: 200ml
- **Coffee**: 100g

---

## Payment System

The coffee machine uses a simple coin-based payment system. Users must insert coins to pay for their drink.

### Accepted Coins:

- **Quarters**: $0.25 each
- **Dimes**: $0.10 each
- **Nickels**: $0.05 each
- **Pennies**: $0.01 each

### Payment Steps:

1. The user inserts coins.
2. The program calculates the total amount.
3. If the inserted amount is sufficient:
   - The machine provides change if overpaid.
   - The drink is prepared and served.
4. If the amount is insufficient:
   - The program refunds the coins and cancels the order.

---

## Future Updates

The program contains several TODO comments, indicating planned improvements or additions:

1. **Expand the Drink Menu**: Add more drink options with new ingredients.
2. **Implement a Persistent Bank**: Allow the machine’s bank balance to persist across runs.
3. **Optimize Resource Deduction and Refill**: Include features for refilling resources manually.
4. **Enhance User Interface**: Implement a graphical or web-based interface for more user-friendly operation.
5. **Refills Resources**:  Implement a method to restore/update resources
---

## How to Run

1. Download or clone the repository containing the Python script.
2. Ensure you have Python installed on your system (Python 3.6 or higher is recommended).
3. Run the script using:
```shell script
python coffee_machine.py
```
4. Follow the interactive menu prompts to use the coffee machine!

**Enjoy your coffee! ☕**

