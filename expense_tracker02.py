class Expense:
    def __init__(self, id, category, amount):
        self.id = id
        self.category = category
        self.amount = amount

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
            print(f'{expense.id}. {expense.category} - {expense.amount}')
    
    def cal_total(self):
        result = 0
        for expense in self.expenses:
            result += expense.amount
        print("Total: ", result)
    

e_tracker = ExpenseTracker()
while True:
    print("""
    1. Add Expense
    2. Update Expense
    3. Delete Expense
    4. Print Expense
    5. Find Total Expenses
    6. Exit
    """)
    operation = int(input("Enter the operation: "))
    match operation:
        case 1:
            e_tracker.add_expense()
        case 2:
            expense_id = int(input("which id's amount do you want to update: "))
            amount = int(input(f"Updated amount for {expense_id}"))
            e_tracker.update_expense(expense_id, amount)
        case 3:
            expense_id = int(input("which id's amount do you want to delete: "))
            e_tracker.del_expense(expense_id)
        case 4:
            e_tracker.print_expenses()
        case 5:
            e_tracker.cal_total()
        case 6:
            print("Exit.....")
            break

print("Expenses calculations are done.")
        
