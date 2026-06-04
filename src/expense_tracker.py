from expense import Expense
import json
from pathlib import Path


class ExpenseTracker:
    
    def __init__(self):
        self.expenses = []
        self.next_id = 1
        self.DATA_FILE = Path(__file__).parent.parent / "data" / "expenses.json"

    # Save the Expenses in JSON format so that it can be used when the program closes still they're saved in .json file
    def save_to_json(self):
        json_expenses = []
        for expense in self.expenses:
            json_expenses.append(expense.to_dict())
        with open(self.DATA_FILE, "w") as file:
            json.dump(json_expenses, file, indent=4)    
        print("File Created Succesfully!!")
    def load_from_json(self):
        
        try:
            with open(self.DATA_FILE, "r") as file:
                data = json.load(file)

                for expense_data in data:
                    expense = Expense.from_dict(expense_data)
                    self.expenses.append(expense)

                if self.expenses:
                    self.next_id = max(expense.id for expense in self.expenses) + 1
            print("Succesfully! JSON File loaded")
        except FileNotFoundError as _:
            print("This is the first attemt and due to that the file is not available to load")
    def add_expense(self):
        try: 
            category = input("Category: ")
            amount = int(input("Amount: "))
            expense = Expense(self.next_id,category,amount)
            self.expenses.append(expense)
            self.next_id += 1
            self.save_to_json()
        except ValueError as e:
            print(f"Please enter the amount in integer format")
        

    def update_expense(self, expense_id, amount):
        for expense in self.expenses:
            if expense.id == expense_id:
                expense.amount = amount
                self.save_to_json()
                return
        print("Incorrect Id")

    def del_expense(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                self.expenses.remove(expense)
                self.save_to_json()
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

             