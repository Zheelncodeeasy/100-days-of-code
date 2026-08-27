# DATA
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


# MAIN CODE

def fetch_resources(money):
    """
     Display Resources
    """
    print(f"Water : {resources['water']}")
    print(f"Milk : {resources['milk']}")
    print(f"Coffee : {resources['coffee']}")
    print(f"Money : ${money}")

def check_resources(choice, money):
    """
    Parameters : user choice, money
    Returns False if insufficent resources and money, else returns change and money
    """

    req_resource = MENU.get(choice)
    ingreds = req_resource['ingredients']
    cost = req_resource['cost']

    # RETURNS FALSE WHEN RESOURCES ARE INSUFFICIENT
    for k, v in ingreds.items():
        if v > resources.get(k, 0):
            print(f"Sorry there is not enough {k}.")
            return False

    processed = process_coins(cost, money)

    # RETURNS FALSE WHEN MONEY IS NOT ENOUGH
    if not processed:
        print("Sorry that's not enough money. Money refunded.")
        return False

    change, money = processed  # UNPACKING TUPLE

    # UPDATING RESOURCES BASED ON SUFFICIENT RESOURCES AND MONEY
    for k, v in ingreds.items():
        resources[k] -= v
    return change, money


def process_coins(price : float , money: float):
    """
    Prompts for coin counts and validates payment against `price`.
    Returns (change, money) if payment is sufficient, otherwise False.
    """

    print("Please insert coins. ")
    while True:
         try:
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickles = int(input("How many nickles? "))
            pennies = int(input("How many pennies? "))

            # COIN COUNTS MUST BE NON-NEGATIVE
            if quarters < 0 or dimes < 0 or nickles < 0 or pennies < 0:
                print("Please enter non-negative numbers.")
                continue

            total = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies

            # NOT ENOUGH MONEY, RETURN FALSE
            if total < price:
                return False
            # MORE MONEY, THEN GIVE CHANGE
            else:
                change = total - price
                money += price
                return change, money

         except ValueError:
            print("Invalid input. Try again.")


def make_coffee():
    money = 0.0
    another_coffee = True

    # TAKE USER INPUT
    while another_coffee:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()

        # TURN OFF THE MACHINE TO BREAK FROM THE LOOP
        if user_choice == "off":
            break
        # CHECK THE RESOURCES
        elif user_choice == "report":
            fetch_resources(money)
        elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
            # CHECK ENOUGH RESOURCES AND MONEY
            result = check_resources(user_choice, money)  # RETURNS FALSE OR TUPLE
            if result:
                change, money = result
                msg = f"Here is your {user_choice} ☕️. Enjoy!"
                if change > 0:
                    print(f"Here is your change: {change:.2f}") # CHANGE GREATER THAN 0
                    print(msg)
                else:
                    print(msg)
        else:
            print("Invalid choice. Try again.") # USER CHOICE INVALID


if __name__ == "__main__":
    make_coffee()


