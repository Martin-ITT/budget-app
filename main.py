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
        try:
            name = input("Please enter category name - min 3 characters: ")
            value = int(input("Please enter budget: "))
            if name in names or len(name) < 3 or name.isspace():
                print("Error, name already exists, is not long enough or is blank. Category not created.")
                wait_here()
            else:
                budgets.append(Budget(name, value))
                names.append(name)
                print(f"Category {name} created. Budget: {value}.")
                wait_here()
        except ValueError:
            print("Error. Invalid input!")
            wait_here()

    elif selection == 2:
        clear()
        try:
            print("Make withdrawal.")
            name = input("Please enter category name to withdraw from: ")
            if name in names:
                value = int(input("Please enter amount to withdraw: "))
                for budget in budgets:
                    if budget.name == name:
                        budget.withdraw(value)
                print(f"€ {value} withdrawn from {name} successfully!")
                wait_here()
            else:
                print("Uknown category. Withdrawal not processed!")
                wait_here()
        
        except ValueError:
            print("Error. Invalid input! Withdrawal not processed!")
            wait_here()

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
        wait_here()

    elif selection == 6:
        clear()
        print("Thank you for using BM software. Bye!")
        control = False
    
    else:
        clear()
        print("Invalid option.")