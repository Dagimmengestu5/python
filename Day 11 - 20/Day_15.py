################# Coffee matssion  ##########################
menu = {
    "buna": {
        "ingredients": {
            "water": 50,
            "salt": 5
        },
        "cost": 1.5
    },
    "shay": {
        "ingredients": {
            "water": 50,
            "salt": 5
        },
        "cost": 1.5
    },
    "weha": {
        "ingredients": {
            "water": 50,
            "salt": 5
        },
        "cost": 1.5
    }
}

resources = {
    "water": 100,
    "milk": 200,
    "coffee": 150,
    "salt": 20
}

payment = 0
profit = 0
is_on = True
def is_resorce_sufficent(order):
    for item in order:
        if order[item] >= resources[item]:
            print(f"sorry their is not enough {item}")
            return False
    return True
def process_coins():
    """return total calculated"""
    print("please insert coins")
    total = int(input("how money quarters: ")) * 0.25
    total += int(input("how money dimes: ")) * 0.1
    total += int(input("how money nickles: ")) * 0.85
    total += int(input("how money pennies: ")) * 0.01
    return total

def mack_drink(drinnk, order):
    for item in order:
        resources[item] -= order[item]
    print(f"hear is your {drinnk}🍵 enjoy it ")


def is_transaction_success(money_recived, drink_cost):
    if money_recived >= drink_cost:
        ch = round(money_recived - drink_cost, 2)
        print(f"Here is ${ch} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry that's not enough money." )
        return False
while is_on:
    choice = input("What would you like? buna/shay/weha: ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources["water"]}ml")
        print(f"milk: {resources["milk"]}ml")
        print(f"coffee: {resources["coffee"]}g")
        print(f"money: ${profit}")
    else:
        drink = menu[choice]
        if is_resorce_sufficent(drink["ingredients"]):
            payment = process_coins()
        if is_transaction_success(payment, drink["cost"]):
            mack_drink(choice, drink["ingredients"])