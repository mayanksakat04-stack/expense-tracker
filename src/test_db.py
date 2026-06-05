# test_db.py

from database import get_connection
import psycopg2
try: 
    conn = get_connection()

    category = input("Enter the category: ")
    amount = int(input("Enter the amount: "))
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO expenses (category, amount)
        VALUES (%s, %s)
        """,
        (category, amount)
    )
    conn.commit()
    cursor.execute("SELECT * from expenses")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    print("The items added successfully into the database")

    
    cursor.close()
    conn.close()
except psycopg2.Error as e:
    print("Database Error:", e)
