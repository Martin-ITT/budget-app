# Goal: “Create a Budget class that can instantiate objects based on different budget categories like food, clothing,
# and entertainment. These objects should allow for depositing and withdrawing funds from each category, as well
# computing category balances and transferring balance amounts between categories”

# Considerations: this is a very interesting project as it allows not only to comprehend how a class is initialized
# and used, but also represented and used as input to other functions. You will learn how to add methods to your
# classes and print them in a way that allows complex representation of your class object at different points in the
# program. As a bonus, you will define a function that computes how much money you are spending across class categories
# as a % of your total expenses, something that can be very useful for the money-savvy programmers among you.

# Approach: define the purpose and flexibility of a class object; build its class methods using a modular approach and
# develop an understanding for how different instances of the same class can interact.

# Key concepts: Class initialization, instance methods and instance representation. Defining and using functions that
# take class instances as input parameters

# https://github.com/ShreyasSubhedar/fcc-budget-app/blob/master/budget.py

class Budget():
    num_of_categories = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        Budget.num_of_categories += 1

    def __repr__(self):
        return f'Name: {self.name}, balance: {self.balance}'

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            return amount
        else:
            raise TypeError("Error. Not enough funds.")

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        self.withdraw(category.deposit(amount))
