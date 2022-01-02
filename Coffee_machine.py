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
    "Money": 0
}


def resource(drink, resources):
    """ checking for the resources in the machine if the coffe should made or not"""
    x = MENU[drink]["ingredients"]
    count = 0
    for w in x:
        if (x[w] <= resources[w]):
            count = count + 1
        else:
            print(f"Their is no enough {w} in the machine")
            return (0)
    if (count == len(x)):
        return (1)


def totaldollors(P, N, D, Q):
    """calucalte the number of dollors"""
    dol = 0
    dol += (P * 0.01)
    dol += (N * 0.05)
    dol += (D * 0.1)
    dol += (Q * 0.25)
    return (dol)


def givedo(dol, drink, resource):
    """ this function with add moeny which we got by making coffee or tell the money is sufficent to the coffee the user asked"""
    z = MENU[drink]["cost"]
    if ((dol - z) >= 0):
        resource["Money"] = resource["Money"] + round(dol - z, 2)
        return (round(dol - z, 2))
    else:
        print(f"Sorry insuffiecent amount is given {round(dol, 2)},money has refunded")
        return (-1)


def re(resources, drink):
    """this  function will calucate the remaining resources which will help ous to make coffee"""
    x = MENU[drink]["ingredients"]
    for q in x:
        resources[q] = resources[q] - x[q]
    return (resources)

count = 0
flage = True
drink = input("what would you like? (espresso/latte/cappuccino): ")
while (flage == True):
    if(drink=='off'):
        flage=False
        print("Machine is off")
    elif(drink=='report'):
        print(resources)
        flage=False

    else:
        p = resource(drink, resources)
        if (p == 1):
                   print("please insert coins")
                   q = int(input("how many quaters?:"))
                   d = int(input("how many dimes?:"))
                   n = int(input("how many nickles?:"))
                   p = int(input("how many pinnies?:"))
                   dollors = totaldollors(p, n, d, q)
                   ret = givedo(dollors, drink, resources)
                   if (ret != -1):
                        resources = re(resources, drink)
                        print(f"Here is ${ret} in change.")
                        print(f"here id your {drink} Enjoy")
                        drink = input("what would like? (espresso/latte/cappuccino):")

                   else:
                           drink = input("what would like? (espresso/latte/cappuccino):")
                           if (drink in MENU.keys()):
                                     flage = True



        else:
                drink = input("what would like? (espresso/latte/cappuccino):")
                if (drink in MENU.keys()):
                         flage = True


