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
    def __init__(self, category):
        self.category = category
        self.amount = 0
        self.add_income()
        self.print_income()

    def __str__(self):
        return + self.category.name.capitalize() + "category. Amount: $" + str(self.amount)

    def add_income(self):
        self.amount = int(
            input("Enter " + self.category.name + " income amount:"))

    def print_income(self):
        print("The amount is", self.amount)

    def get_category(self):
        return self.category.name.capitalize() + " Income Amount: $" + str(self.amount)
# ----------------------------------------------*** CODE GOES HERE ***----------------------------------------------
# CODE FOR EXPENSE
expenselst = []
while True:
    i = input("Add Expense?[yes/no]:")
    if i == "yes":
        expenselst.append(
            Expense(ExpenseCategory[input("Enter category name:")]))
    elif i == "no":
        break
    else:
        print("Enter a valid answer!")
for i in expenselst:
    print(i)

b = 0
while True:
    input_1 = input("Sum up expense?[yes/no]:")
    if input_1 == "yes":
        for i in expenselst:
            b += i.price
        print("Your expense sum is $", b, ".")
        break
    elif input_1 == "no":
        break
    else:
        print("Enter valid answer:")

# CODE FOR INCOME
income_list = []
income_amount = []
while True:
    n = input("Add income?[yes/no]:")
    if n == "yes":
        income_list.append(
            Income(IncomeCategory[input("Enter income type: ")]))
    elif n == "no":
        break
    else:
        print("Enter a valid answer:[yes/no]")

for i in income_list:
    print(i.get_category())

# SUM OF INCOME
k = 0
while True:
    input_2 = input("Sum up income?[yes/no]:")
    if input_2 == "yes":
        for i in income_list:
            k += i.amount
            break
        print("The sum is:","$", k)
    elif input_2 == "no":
        break
    else:
        print("Enter valid answer!")
# DELETE INCOME
    for i in income_list:
        input_3 = input("Delete an income?[yes/no]:")
        if input_3 == "yes":
            an_input = input("Which one?:")
            if an_input == "job":
                income_list.remove(i)
            elif an_input == "allowance":
                income_list.remove(i)
            elif an_input == "loan":
                an_input.remove(i)
            elif an_input == "other":
                an_input.remove(i)
        elif input_3 == "no":
            break
        else:
            break


# SHOW ALL INCOMES
for i in income_list:
    print(i.get_category())

# GET TOTAL SUM
for i in expenselst and income_list:
    input_4 = "Get total net?[yes/no]:"
    if input_4 == "yes":
        print(b - k)