from expense import Expense

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.next_id = 1

    def add_expense(self):
        try: 
            category = input("Category: ")
            amount = int(input("Amount: "))
            expense = Expense(self.next_id,category,amount)
            self.expenses.append(expense)
            self.next_id += 1
        except ValueError as e:
            print(f"Please enter the amount in integer format")
        

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
        return result
    
    def get_unique_categories(self):
        categories = set()

        for expense in self.expenses:
            categories.add(expense.category)
        return categories

    def search_by_category(self, category):
        found = False
        for expense in self.expenses:
            if expense.category == category:
                print(expense)
                found = True
        if not found: print("Invalid Category")

    def category_totals(self):
        category_expenses = {}
        for expense in self.expenses:
            if expense.category not in category_expenses:
                category_expenses[expense.category] = expense.amount
            else:
                category_expenses[expense.category] += expense.amount
        
        for category, amount in category_expenses.items():
            print(f"{category} = {amount}")
    def highest_expense(self):
        if not self.expenses:
            print("No expenses found")
            return 
        max_expense = self.expenses[0]
        for expense in self.expenses:
            if expense.amount > max_expense.amount:
                max_expense = expense
        
        print("Highest Expense:")
        print(max_expense)
    
    def average_expense(self):
        if len(self.expenses) == 0:
            print("No expenses found")
            return
        avg_exp = self.cal_total() / len(self.expenses)
        print("Average Expense = ",avg_exp)

             