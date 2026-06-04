from expense_tracker import ExpenseTracker


e_tracker = ExpenseTracker()
e_tracker.load_from_json()
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
    10. Exit
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
            print("Total: ", e_tracker.cal_total())
        case 6:
            expense_categories = e_tracker.get_unique_categories()
            if len(expense_categories) == 1:
                expense_category = list(expense_categories)[0]
                e_tracker.search_by_category(expense_category)
            else:
                expense_category = input("Enter the name of category that you want to search: ")
                e_tracker.search_by_category(expense_category)
        case 7:
            e_tracker.category_totals()
        case 8:
            e_tracker.highest_expense()
        case 9:
            e_tracker.average_expense()
        case 10:
            e_tracker.save_to_json()
            print("All Expenses are saved to JSON\nExit.....")
            break

print("Expenses Tracker Window is closed now...")
        
