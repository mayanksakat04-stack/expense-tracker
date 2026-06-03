from expense import Expense

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.next_id = 1

    def add_expense(self):
        category = input("Category: ")
        amount = int(input("Amount: "))
        expense = Expense(self.next_id,category,amount)
        self.expenses.append(expense)
        self.next_id += 1

    def update_expense(self, expense_id, amount):
        for expense in self.expenses:
            if expense.id == expense_id:
                expense.amount = amount
                return
        print("Incorrect Id")

    def del_expense(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                self.expenses.remove(expense)
                return
        print("Incorrect Id")
    
    def print_expenses(self):
        for expense in self.expenses:
            print(expense)
    


    def cal_total(self):
        result = 0
        for expense in self.expenses:
            result += expense.amount
        print("Total: ", result)