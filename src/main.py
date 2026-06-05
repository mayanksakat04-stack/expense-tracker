from expense_tracker import ExpenseTracker


e_tracker = ExpenseTracker()
# e_tracker.load_from_json()
while True:
    print("""
    1. Add Expense
    2. Update Expense
    3. Delete Expense
    4. Print Expense
    5. Find Total Expenses
    6. Search by Category
    7. Category Totals
    8. High Expense
    9. Average Expense
    10. Search Expense by id
    11. Exit
    """)
    operation = int(input("Enter the operation: "))
    match operation:
        case 1:
            try:
                category = input("Category: ")
                amount = int(input("Amount: "))
                e_tracker.add_expense(category, amount)
            except ValueError:
                print("Amount must be an integer")
        case 2:
            try:
                expense_id = int(input("which id's amount do you want to update: "))
                amount = int(input(f"Updated amount for {expense_id}"))
                e_tracker.update_expense(expense_id, amount)
            except ValueError:
                print("Amount and expense_id should be an integer")
        case 3:
            try:
                expense_id = int(input("which id's amount do you want to delete: "))
                e_tracker.del_expense(expense_id)
            except ValueError:
                print("expense_id should be an integer")
        case 4:
            e_tracker.print_expenses()
        case 5:
            print("Total: ", e_tracker.cal_total())
        case 6:
            expense_category = input("Enter the category: ")
            e_tracker.search_by_category(expense_category)
        case 7:
            e_tracker.category_totals()
        case 8:
            e_tracker.highest_expense()
        case 9:
            e_tracker.average_expense()
        case 10:
            try:
                expense_id = int(input("which id's amount do you want to update: "))
                e_tracker.get_expense_by_id(expense_id)
            except ValueError:
                print("expense_id should be an integer")
        case 11:
            print("All Expenses are saved to JSON\nExit.....")
            break

print("Expenses Tracker Window is closed now...")
        
