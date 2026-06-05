# from expense import Expense
import json
from pathlib import Path
from database import get_connection
import psycopg2
class ExpenseTracker:
    
    def __init__(self):
        pass
    
    # POSTGRESQL CONNECTION
    def connect_db(self):
        try:
            return get_connection()
        except psycopg2.Error as e:
            print("Error in Database Connection: \n",e)
            return None

    def add_expense(self, category, amount):
        conn = None
        cursor = None
        try: 
            conn = self.connect_db()
            if conn is None:
                return None
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO expenses (category, amount) VALUES (%s, %s)   
                """, (category, amount))
            conn.commit()
            print("Expense added successfully!")
        except ValueError:
            print(f"Amount must be an integer.")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def update_expense(self, expense_id, amount):
        conn = None
        cursor = None
        try: 
            conn = self.connect_db()
            if conn is None:
                return None
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE expenses SET amount = %s WHERE id = %s
                """, (amount, expense_id))
            conn.commit()
            print("Expense updated successfully!")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def del_expense(self, expense_id):
        conn = None
        cursor = None
        try:
            conn = self.connect_db()
            if conn is None:
                return None
            cursor = conn.cursor()
            cursor.execute("""
                DELETE from expenses WHERE id = %s;
                """, (expense_id,))
            conn.commit()
            print("Expense deleted successfully!")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
    
    def print_expenses(self):
        conn = None
        cursor = None
        try:
            conn = self.connect_db()
            if conn is None:
                return None
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * from expenses;
                """)
            print("EXPENSES: \n")
            rows = cursor.fetchall()
            if not rows:
                print("No Expenses found")
                return
            for id, category, amount in rows:
                print(f"{id}. {category} - ₹{amount}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
            
    
    def cal_total(self):
        conn = None
        cursor = None

        try:
            conn = self.connect_db()
            if conn is None:
                return None
            cursor = conn.cursor()
            cursor.execute("""
                SELECT SUM(amount) from expenses;
                """)
            print("Total: \n")
            row = cursor.fetchone()
            if row is not None:
                total = row[0]
                print("Total:", total)
            else:
                print("No expenses found.")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def search_by_category(self, category):
        conn = None
        cursor = None
        try: 
            conn = self.connect_db()
            if conn is None:
                return None
            cursor = conn.cursor()
            cursor.execute("""
                SELECT category, amount FROM expenses WHERE category = %s;
                """, (category,))
            print(f"Searched data for Category: {category}\n")
            rows = cursor.fetchall()
            if not rows:
                print("No Expenses found")
                return
            for row in rows:
                print(row)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def category_totals(self):
        conn = None
        cursor = None
        try:
            conn = self.connect_db()
            if conn is None:
                return None
            cursor = conn.cursor()
            cursor.execute("""
                SELECT category, SUM(amount) from expenses GROUP BY category
                """, )
            print(f"Fetched all category total:\n")
            rows = cursor.fetchall()

            if not rows:
                print("No Expenses found")
                return
            for row in rows:
                print(row)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def highest_expense(self):
        conn = None
        cursor = None

        try:
            conn = self.connect_db()
            if conn is None:
                return None
            cursor = conn.cursor()
            cursor.execute("""
                SELECT MAX(amount) from expenses;
                """)

            row = cursor.fetchone()
            if row is not None:
                highest = row[0]
                print("Highest Expense:", highest)
            else:
                print("No expenses found.")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
    
    def average_expense(self):
        conn = None
        cursor = None

        try:
            conn = self.connect_db()
            if conn is None:
                return None
            cursor = conn.cursor()
            cursor.execute("""
                SELECT AVG(amount) from expenses;
                """)
            row = cursor.fetchone()
            if row is not None:
                average = row[0]
                print("Average Expense:", average)
            else:
                print("No expenses found.")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
    def get_expense_by_id(self, expense_id):
        conn = None
        cursor = None

        try:
            conn = self.connect_db()
            if conn is None:
                return None
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, category, amount from expenses where id = %s;
                """, (expense_id,))
            row = cursor.fetchone()

            if row is None:
                print("No expense found")
                return

            id, category, amount = row
            print(f"{id}. {category} - ₹{amount}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

             