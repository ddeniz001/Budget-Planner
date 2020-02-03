# This program is written for the sole purpose of teaching you to be smarter with your budget.

from enum import Enum

import budgetClasses


# ----------------------------------------------*** CODE GOES HERE ***----------------------------------------------
expenselst = []
income_list = []
income_amount = []

# 1. Main menu; User picks an option.
while True:
    Options = input(
        """Welcome to Budget Planner. What would you like to do?\n
        1 - Add expense\n
        2 - Add income \n
        3 - List incomes \n
        4 - List expense\n
        5 - Sum up incomes\n
        6 - Sum up expenses\n
        7 - Delete expense\n
        8 - Delete income\n
        9 - Get your net\n
        10 - Exit\n""")
# 2. Add Expense
    if Options == "1":
        inp_1 = input("Add Expense? [yes/no]: ")
        if inp_1 == "yes":
            while True:
                try:
                    expenselst.append(
                        Expense(ExpenseCategory[input("Enter category name from the list below.\n"
                                                      "1 - groceries\n2 - entertainment\n3 - memberships\n4 - utilities\n5 - rent\n6 - other")]))
                    break
                except KeyError:
                    print("Please Enter Valid Input!")
        elif inp_1 == "no":
            break
        else:
            print("Enter a valid answer!")


# Fix this later
# 3. Add Income
    elif Options == "2":
        inp_6 = input("Add Income? [yes/no]: ")
        if inp_6 == "yes":
            while True:
                try:
                    income_list.append(
                        Income(IncomeCategory[input("Type in the category name from the list below.\n"
                                                    "1 - job\n2 - allowance\n3 - loan\n4 - other\n5 - scholarship\n")]))
                    break
                except KeyError:
                    print("Please enter a valid input.")
        elif inp_6 == "no":
            break
        else:
            print("Enter a valid answer!!")
        input_3 = input("Delete an income item? [yes/no]: ")
# 4. List Income
    elif Options == "3":
        for i in income_list:
            print(str(income_list.index(i)) + " " + i.getCategory())
# 5. List Expense
    elif Options == "4":
        for i in expenselst:
            print(str(expenselst.index(i)) + " " + i.getCategory())
# 6. Sum Income
    elif Options == "5":
        input_2 = input("Sum up income? [yes/no]: ")
        if input_2 == "yes":
            k = 0
            for i in income_list:
                k += i.amount
            print("The sum is:", "$", k)
        elif input_2 == "no":
            print("Why the fuck did you choose me then?")
# 7. Sum Expense
    elif Options == "6":
        inp_4 = input("Sum up expenses? [yes/no]: ")
        if inp_4 == "yes":
            b = 0
            for i in expenselst:
                b += i.price
            print("The sum for expense is: $", + b)
        elif inp_4 == "no":
            print("Fuck you then! Why da fuck did you click on me?")
        else:
            print("Enter a valid answer please.")
# 8. Delete Expense
    elif Options == "7":
        inp_2 = input("Delete expense? [yes/no]:")
        if inp_2 == "yes":
            for i in expenselst:
                print((str(expenselst.index(i)) + " " + i.getCategory()))
            inp_a = input("Which one?:")
            del expenselst[int(inp_a)]
        elif inp_2 == "no":
            print("Go Back")
# 9. Delete Income
    elif Options == "8":
        if input_3 == "yes":
            for i in income_list:
                print(str(income_list.index(i)) + " " + i.getCategory())
            an_input = input("Which one?:")
            del income_list[int(an_input)]
        elif input_3 == "no":
            print("Go Back")

# 10. Get Total Net
    elif Options == "9":
        net = (k - b)
        inp_5 = input("Get your net? [yes/no]: ")
        if inp_5 == "yes":
            print(net)
        elif net > 0:
            print("Congrats! On a monthly basis, you are saving ", "$", net)
        elif net < 0:
            print(
                "Ouch. On a monthly basis, you're in the negative, with an integer of ", "$", net)

    elif Options == None:
        pass
