import os
import time
from budget import Budget

control = True # loop control
clear = lambda: os.system('cls') # clear console
budgets = [] #  list of objects
names = [] # list of categories

def wait_here():
    time.sleep(3)
    clear()

while control:
    print("--------------------")
    print("Budget manager v 1.0")
    print("--------------------")
    print("--------------------")
    print("---- Main Menu -----")
    print("--------------------")
    print(" Create category: 1 ")
    print(" Make withdrawal: 2 ")
    print(" Make lodgement:  3 ")
    print(" Make transfer:   4 ")
    print(" View categories: 5 ")
    print(" Exit:            6 ")
    print("--------------------")

    selection = int(input("Please select: "))
    if selection == 1:
        clear()
        print("Create a category.")
        name = input("Please enter category name: ")
        value = int(input("Please enter budget: "))
        
        if name in names:
            print("Error, name already exists. Category not created.")
            wait_here()
        else:
            budgets.append(Budget(name, value))
            names.append(name)
            print(f"Category {name} created. Budget: {budget}.")
            wait_here()
        # print(f"Category {name} created.")
        # print(name.balance)

    elif selection == 2:
        clear()
        print("Make withdrawal.")
        print(budgets)

    elif selection == 3:
        clear()
        print("Make lodgement.")

    elif selection == 4:
        clear()
        print("Make transfer.")

    elif selection == 5:
        clear()
        print("View categories.")
        for budget in budgets:
            print(budget)

    elif selection == 6:
        clear()
        print("Thank you for using BM software. Bye!")
        control = False
    
    else:
        clear()
        print("Invalid option.")