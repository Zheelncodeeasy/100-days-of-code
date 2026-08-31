import money_machine
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# creating objects from different class
menu_items = Menu()
make_coffee = CoffeeMaker()
process_transaction = MoneyMachine()

# flag variable
another_coffee = True

while another_coffee:
    # options
    options = menu_items.get_items()
    # Take coffee order from user
    user_order = input(f"What would you like? ({options}): ").strip().lower()

    # off to shut down the coffee machine
    if user_order == "off":
        another_coffee = False
    # display ingredients
    elif user_order == "report":
        make_coffee.report()
        process_transaction.report()
    else:
        # find coffee drink
        check_drink = menu_items.find_drink(user_order)
        # if drink exists
        if check_drink:
            enough_resources = make_coffee.is_resource_sufficient(check_drink)  # checks sufficient resources
            if enough_resources:
                enough_money = process_transaction.make_payment(check_drink.cost) # checks sufficient money
                # if both resources and money is enough then make coffee
                if enough_money:
                    make_coffee.make_coffee(check_drink)
