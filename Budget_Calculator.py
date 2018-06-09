import budget_classes

Options = int(input("Welcome to Budget Calculator. Please choose an option:\n 1 - "
                "Add expense:\n 2 - "
                "Add income:\n 3 - "
                "List expenses:\n 4 - "
                "List income:\n 5 - "
                "Delete Expense:\n 6 - "
                "Delete Income:\n 7 - "
                "Sum expense:\n 8 - "
                "Sum income:\n 9 - "
                "Sum everything:\n 10 - "
                "Show Graph:\n 11 - "
                "Save & Exit\n 12 - "
                "Exit "))
if Options == 1:
    inp = input('Enter money spent for the type of expense.'
                    'Enter Groceries\n 1 - '
                    'Enter Entertainment\n 2 - '
                    'Enter Memberships\n 3 - '
                    'Enter Utilities\n 4 -'
                    'Enter Rent\n 5 - '
                    'Other 6')
    if inp == "1":
        expense = budget_classes.Expense()
        expense.print_expense()
elif Options == 2:
    print(int(input('Enter Income:\n 1 - '
                    "Job\n 2 - "
                    'Enter Scholarship\n 3 - '
                    'Enter Allowance\n 4 - '
                    'Enter Loan\n 5 -'
                    'Enter Other\n 6 - ')))
    if i == "2":
        income = budget_classes.Income()
        income.print_income()

elif Options == 3:
    print(int(input('List expenses ')))

elif Options == 4:
    print(int(input('List incomes')))

elif Options == 5:
    print(int(input('Delete expense')))

elif Options == 6:
    print(int(input('Delete income')))

elif Options == 7:
    print(int(input('Sum expense')))

elif Options == 8:
    print(int(input('Sum income')))

elif Options == 9:
    print(int(input('Sum everything')))

elif Options == 10:
        print(int(input('Show graph')))

elif Options == 11:
    print(int(input("Save & exit")))

elif Options == 12:
    print(int(input("Exit")))