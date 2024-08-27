money = 0 

def report():
    global money
    for key, value in resources.items():
        print(f"{key}: {value}")
    print(f"Money: ${money}")

def drink(answer):
    global resources
    global money
    money_inputted = coins()
    possible = True
    if money_inputted < MENU[answer]['cost']:
        print("Sorry, you don't have enough money.")
        possible = False
    if possible and check_possibility(answer):
        for key, value in resources.items():
            resources[key] -= MENU[answer]['ingredients'][key]
        money += MENU[answer]['cost']
        print(f"Here is ${money_inputted - MENU[answer]['cost']} in change")
    else:
        print('Sorry this transaction is not possible')



def check_possibility(answer):
    possibility = True
    global resources
    for key, value in resources.items():
        if resources[key] < MENU[answer]['ingredients'][key]:
            possibility = False
        if possibility == False:
            break
    return possibility


def coins():
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))
    total_money = quarters*.25 + dimes*.1 + nickles*.5 + pennies*.01
    return total_money


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


answer = ''

while not answer == 'off':
    answer = input('What would you like? (espresso/latte/cappuccino):')
    if answer == 'off':
        break
    elif answer == 'report':
        report()
    elif answer in MENU:
        drink(answer)