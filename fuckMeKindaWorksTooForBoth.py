from enum import Enum

#------------------------------------------- *** EXPENSE CLASS *** ---------------------------------------------------#


class ExpenseCategory(Enum):
    groceries = 1
    entertainment = 2
    memberships = 3
    utilities = 4
    rent = 5
    other = 6


class Expense:
    def __init__(self, category):
        self.category = category
        self.price = 0
        self.add_expense()
        self.print_expense()
        self.expense = 0

    def add_expense(self):
        self.price = int(input('Enter ' + self.category.name + " price:"))

    def print_expense(self):
        print("The price is, ", self.price)

    def __str__(self):
        return self.category.name.capitalize() + " Price: $" + str(self.price)

    def expenseSum(self):
        return "Expense sum is:" + self.category.price


#---------------------------------------------*** INCOME CLASS ***----------------------------------------------------#
class IncomeCategory(Enum):
    job = 1
    allowance = 2
    loan = 3
    other = 4
    scholarship = 5


class Income:
    def __init__(self, category, amount=None):
        self.category = category
        self.amount = amount
        if (amount == None):
            self.add_income()
        self.print_income()

    def __str__(self):
        return + self.category.name.capitalize() + "category. Amount: $" + str(self.amount)

    def add_income(self):
        self.amount = int(
            input("Enter " + self.category.name + " income amount:"))

    def print_income(self):
        print("The amount is $", self.amount)

    def get_category(self):
        return self.category.name.capitalize() + " Income Amount: $" + str(self.amount)


# ----------------------------------------------*** CODE GOES HERE ***----------------------------------------------

Options = input(
    "Wtf do you want?\n"
    "1 - Sum up incomes\n"
    "2 - Delete income \n"
    "3 - List incomes \n"
    "4 - Add income\n"
    "5 - Add expense\n"
    "6 - List expense\n"
    "7 - Delete expense\n"
    "8 - Sum up expenses\n"
    "9 - Get your net\n"
    "10 - Go and **** yourself\n")

# CODE FOR EXPENSE
expenselst = []
while True:
    if Options == "5":
        inp_1 = input("Add Expense?[yes/no]:")
        if inp_1 == "yes":
            while True:
                try:
                    expenselst.append(
                        Expense(ExpenseCategory[input("Enter category name:")]))
                    break
                except KeyError:
                    print("Please Enter Valid Input!")
        elif inp_1 == "no":
            break
        else:
            print("Enter a valid answer!")

    elif Options == "6":
        for i in expenselst:
            print(str(expenselst.index(i)) + " " + i.get_category())

    elif Options == "7":
        inp_2 = input("Delete expense?:[yes/no]")
        if inp_2 == "yes":
            for i in expenselst:
                print((str(expenselst.index(i)) + " " + i.get_category()))
            inp_a = input("Which one?:")
            del expenselst[int(inp_a)]
        elif inp_2 == "no":
            print("WHY did you click on me then?")

    elif Options == "8":
        inp_4 = input("Sum up expenses?:[yes/no]")
        if inp_4 == "yes":
            b = 0
            for i in expenselst:
                b += i.price
            print("The sum for expense is: $", + k)
        elif inp_4 == "no":
            print("Fuck me then! Why da fuck did you click on me?")
        else:
            print("Enter a valid answer!!")

    elif Options == "9":
        inp_5 = input("Get your net?")
        if inp_5 == "yes":
            print(k - b)
    # CODE FOR INCOME
    income_list = []
    income_amount = []
    if Options == "4":
        inp_6 = input("Add Income?[yes/no]:")
        if inp_6 == "yes":
            while True:
                try:
                    income_list.append(
                        Expense(IncomeCategory[input("Enter category name:")]))
                    break
                except KeyError:
                    print("Please Enter Valid Input!")
        elif inp_6 == "no":
            break
        else:
            print("Enter a valid answer!!")


if Options == "1":
    input_2 = input("Sum up income?[yes/no]:")
    if input_2 == "yes":
        k = 0
        for i in income_list:
            k += i.amount
        print("The sum is:", "$", k)
    elif input_2 == "no":
        print("Fuck me then! Why the fuck did you choose this option?")
    else:
        print("Enter valid answer!")

elif Options == "2":
    input_3 = input("Delete an income?[yes/no]:")
    if input_3 == "yes":
        for i in income_list:
            print(str(income_list.index(i)) + " " + i.get_category())
        an_input = input("Which one?:")
        del income_list[int(an_input)]
elif input_3 == "no":
    print("Fuck me then! Why the fuck did you choose this option?")

elif Options == "3":
    for i in income_list:
        print(str(income_list.index(i)) + " " + i.get_category())
elif Options == None:
    pass
else:
    print("Go and FUCK yourself!")
