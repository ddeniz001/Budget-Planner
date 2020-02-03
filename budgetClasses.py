# This program is written for the sole purpose of teaching you to be smarter with your budget.
from enum import Enum

# Main menu function for the program. Enumeration is used for convenience. (Will be added later.)


class menuOptions(Enum):
    SUM_UP_INCOME = 1
    DELETE_INCOME = 2
    LIST_INCOME = 3
    ADD_INCOME = 4
    ADD_EXPENSE = 5
    LIST_EXPENSE = 6
    DEL_EXPENSE = 7
    SUM_EXPENSES = 8
    GET_NET = 9
    EXIT = 10

# Expense options for input. Given values so that the user can type it in themselves.
class ExpenseCategory(Enum):  # Parent Class
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

    def getCategory(self):
        return self.category.name.capitalize() + " Expense Amount: $" + str(self.price)


# Input options for user.
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

    def getCategory(self):
        return self.category.name.capitalize() + " Income Amount: $" + str(self.amount)
