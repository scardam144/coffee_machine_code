import data


# function for money to be taken
def money_taken(coffee):
    print("Please Insert Coins.")
    quarters = int(input("How many Quarters?"))
    dimes = int(input("How many Dimes?"))
    nickels = int(input("How many Nickels?"))
    pennies = int(input("How many Pennies?"))
    print(money_calculation(q_coins=quarters, d_coins=dimes, n_coins=nickels, p_coins=pennies, coffee_of=coffee))


# Calculate money and check changes and add profit.
def money_calculation(q_coins, d_coins, n_coins, p_coins, coffee_of):
    """Fetch coffee type details from dictionary"""
    coffee_cost = data.MENU[coffee_of]['cost']
    total_money = q_coins*0.25 + d_coins*0.10 + n_coins*0.05 + p_coins*0.01
    if total_money > coffee_cost:
        change = total_money - coffee_cost
        data.profit += coffee_cost
        resource_used(coffee_of)
        return f"Here is ${round(change, 2)} in change.\n Here is your {coffee_of}. Enjoy! "
    elif total_money == coffee_cost:
        data.profit += coffee_cost
        resource_used(coffee_of)
        return f"That's the perfect Money you put!.\n Here is your {coffee_of}. Enjoy!"
    else:
        return "Sorry that's not enough money, Money Refunded!"


# check what user inputs and run that function.
def check_input(user_input):
    if user_input == 'off':
        return False
    elif user_input == 'report':
        print(resources_function())
        return True
    else:
        requirement_check(user_input)
        return True


# Resources functions to be printed.
def resources_function():
    water_resource = data.resources['water']
    milk_resource = data.resources['milk']
    coffee_resource = data.resources['coffee']
    return f"Water: {water_resource}ml,\n Milk: {milk_resource}ml,\n Coffee: {coffee_resource}g,\n" \
           f" Money: ${data.profit}"


# Check resource available for coffee for further process.
def requirement_check(coffee_type):
    water_need = data.MENU[coffee_type]['ingredients']['water']
    coffee_need = data.MENU[coffee_type]['ingredients']['coffee']
    milk_need = data.MENU[coffee_type]['ingredients']['milk']
    water_avail = data.resources['water']
    coffee_avail = data.resources['coffee']
    milk_avail = data.resources['milk']
    if water_avail >= water_need:
        if coffee_avail >= coffee_need:
            if milk_avail >= milk_need:
                return money_taken(coffee_type)
            else:
                print("Sorry there is not enough Milk!")
        else:
            print(f"Sorry there is not enough Coffee!")
    else:
        print(f"Sorry there is not enough Water!")


# Deduct the Actual Resource and used Resource function
def resource_used(type_coffee):
    water_need = data.MENU[type_coffee]['ingredients']['water']
    coffee_need = data.MENU[type_coffee]['ingredients']['coffee']
    milk_need = data.MENU[type_coffee]['ingredients']['milk']
    water_avail = data.resources['water']
    coffee_avail = data.resources['coffee']
    milk_avail = data.resources['milk']
    data.resources['milk'] = milk_avail-milk_need
    data.resources['water'] = water_avail-water_need
    data.resources['coffee'] = coffee_avail-coffee_need


# Repeat the process until it ends. main function.
def main_function():
    is_running = True
    while is_running:
        ''' What they Like to take espresso, latte, cappuccino'''
        user_take = input("What would you like? (espresso/latte/cappuccino)").lower()
        ''' check what user inputs and run that function'''
        is_running = check_input(user_take)


main_function()
