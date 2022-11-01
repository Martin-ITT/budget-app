from budget import Budget

control = True

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
    if selection == 6:
        print("Thank you for using BM software. Bye!")
        control = False