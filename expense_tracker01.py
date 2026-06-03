# expenses = []


# def add_expenses(id):
#     category = input("Category: ")
#     amount = int(input("Amount: "))
#     expenses.append({"id": id, "category": category, "amount": amount})

# def update_expense(id, amount):
#     for expense in expenses:
#         if expense["id"] == id:
#             expense["amount"] = amount
#             return
#     print("Incorrect Id")

# def delete_expense(id):
#     for expense in expenses:
#         if expense["id"] == id:
#             expenses.remove(expense)
#             return
#     print("Incorrect Id")
# def print_expenses():
#     for expense in expenses:
#         print(f'{expense["id"]}. {expense["category"]} - {expense["amount"]}')

# def find_total():
#     result = 0
#     for expense in expenses:
#         result += expense["amount"]
#     print(f"Total: {result}")

# next_id = 1
# while True:
#     print("""
#     1. Add Expense
#     2. Update Expense
#     3. Delete Expense
#     4. Print Expense
#     5. Find Total Expenses
#     6. Exit
#     """)
#     operation = int(input("Enter the operation: "))
#     match operation:
#         case 1:
#             add_expenses(next_id)
#             next_id+=1
#         case 2:
#             expense_id = int(input("which id's amount do you want to update: "))
#             amount = int(input(f"Updated amount for {expense_id}"))
#             update_expense(id, amount)
#         case 3:
#             expense_id = int(input("which id's amount do you want to delete: "))
#             delete_expense(expense_id)
#         case 4:
#             print_expenses()
#         case 5:
#             find_total()
#         case 6:
#             print("Exit.....")
#             break

# print("Expenses calculations are done.")
