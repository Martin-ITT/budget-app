import os
import time
import datetime
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
                with open(f"{name}.txt", "w") as file1:
                    time_stamp = datetime.datetime.now()
                    file1.write(f"{time_stamp} Name: {name}, initial budget: {value}. Category created.\n")
                print(f"Category {name} created. Budget: {value}.")
                wait_here()
        except ValueError:
            print("Error. Invalid input!")
            wait_here()

    elif selection == 2:
        clear()
        try:
            print("Make a withdrawal.")
            name = input("Please enter category name to withdraw from: ")
            if name in names:
                value = int(input("Please enter amount to withdraw: "))
                for budget in budgets:
                    if budget.name == name:
                        budget.withdraw(value)
                        new_balance = budget.get_balance()
                with open(f"{name}.txt", "a") as file1:
                    time_stamp = datetime.datetime.now()
                    file1.write(f"{time_stamp} Name: {name}, {value} withdrawn. Balance: {new_balance}.\n")
                print(f"€{value} withdrawn from {name} successfully!")
                wait_here()
            else:
                print("Uknown category. Withdrawal not processed!")
                wait_here()
        
        except ValueError:
            print("Error. Invalid input! Withdrawal not processed!")
            wait_here()

    elif selection == 3:
        clear()
        try:
            print("Make a lodgement.")
            name = input("Please enter category name to make a lodgement: ")
            if name in names:
                value = int(input("Please enter amount to lodge: "))
                for budget in budgets:
                    if budget.name == name:
                        budget.deposit(value)
                        new_balance = budget.get_balance()
                with open(f"{name}.txt", "a") as file1:
                    time_stamp = datetime.datetime.now()
                    file1.write(f"{time_stamp} Name: {name}, {value} lodged. Balance: {new_balance}.\n")
                print(f"€{value} lodged to {name} successfully!")
                wait_here()
            else:
                print("Uknown category. Lodgement not processed!")
                wait_here()
        
        except ValueError:
            print("Error. Invalid input! Lodgement not processed!")
            wait_here()

    elif selection == 4:
        clear()
        try:
            print("Make a transfer.")
            from_name = input("Please enter category name to transfer from: ")
            to_name = input("Please enter category name to transfer into: ")
            if from_name in names and to_name in names:
                value = int(input("Please enter amount to transfer: "))
                for budget in budgets:
                    if budget.name == from_name:
                        budget.withdraw(value)
                        from_value = budget.get_balance()
                    if budget.name == to_name:
                        budget.deposit(value)
                        to_value = budget.get_balance()
                with open(f"{from_name}.txt", "a") as file1:
                    time_stamp = datetime.datetime.now()
                    file1.write(f"{time_stamp} €{value} transfered to {to_name}. Balance: {from_value}.\n")
                with open(f"{to_name}.txt", "a") as file1:
                    time_stamp = datetime.datetime.now()
                    file1.write(f"{time_stamp} €{value} received transfer from {from_name}. Balance: {to_value}.\n")
                print(f"€{value} transfered from {from_name} to {to_name} successfully!")
                wait_here()
            else:
                print("Uknown category. Transfer not processed!")
                wait_here()
        
        except ValueError:
            print("Error. Invalid input! Transfer not processed!")
            wait_here()

    elif selection == 5:
        clear()
        print("View categories.")
        for budget in budgets:
            print(budget)
        time.sleep(2)
        wait_here()

    elif selection == 6:
        clear()
        print("Thank you for using BM software. Bye!")
        control = False
    
    else:
        clear()
        print("Invalid option.")