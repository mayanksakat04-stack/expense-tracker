from expense_tracker import ExpenseTracker


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
        
