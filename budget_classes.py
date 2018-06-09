from enum import Enum

#------------------------------------------- *** EXPENSE CLASS *** ---------------------------------------------------#
class Expense_Category(Enum):
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
        return  self.category.name.capitalize() + " Price: $" + str(self.price)

    def expenseSum(self):
        return "Expense sum is:" + self.category.price




#---------------------------------------------*** INCOME CLASS ***----------------------------------------------------#

class Income_Category(Enum):
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
        return  + self.category.name.capitalize() + "category. Amount: $" + str(self.amount)

    def add_income(self):
        self.amount = int(input("Enter " + self.category.name + " income amount:"))

    def print_income(self):
        print("The amount is", self.amount)

    def getCategory(self):
        return self.category.name.capitalize() + " Income Amount: $" + str(self.amount)






#----------------------------------------------   CODE GOES HERE

    #--------Code for EXPENSE

expenselst = []

while True:
    i = input("Add Expense?[yes/no]:")
    if i == "yes":
        expenselst.append(Expense(Expense_Category[input("Enter category name:")]))
    elif i == "no":
        break
    else:
        print("Enter a valid answer!")

for i in expenselst:
   print(i)

for i in expenselst:
    raw_input = input("Sum up expense?")
    if raw_input == "yes":
        expenselst.sum(Expense_Category)





    #---------Code for INCOME

income_list = []
income_amount = []

x = False
while not x:
    n = input("Add income?[yes/no]:")
    if n == "yes":
        income_list.append(Income(Income_Category[input("Enter income type: ")]))
    elif n == "no":
        break
    else:
      print("Enter a valid answer:[yes/no]")


for i in income_list:
    print(i.getCategory())

for i in income_amount:
    print (sum(i.getIncomeAmount()))








