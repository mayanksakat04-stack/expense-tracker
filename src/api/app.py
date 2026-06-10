from fastapi import FastAPI
# from .db_connection import connect_db
from ..models.schemas import ExpenseSchema, UserSchema, ClientSchema, InvoiceSchema, WalletSchema


from .routers import (
    expenses,
    users,
    clients,
    transactions,
    wallets,
    invoices
)
import psycopg2
from fastapi import HTTPException

app = FastAPI()


app.include_router(expenses.router)
app.include_router(users.router)
app.include_router(clients.router)


# Users 

# @app.get("/users")
# def get_users():
#     conn = None
#     cursor = None
#     try:
#         conn = connect_db()
#         if conn is None:
#             raise HTTPException(
#             status_code=500,
#             detail="Database connection failed"
#         )
#         cursor = conn.cursor()
#         cursor.execute("""
#             SELECT id, username, email, business_type
#             FROM users
#             """,)
#         rows = cursor.fetchall()
#         conn.commit()
#         if not rows:
#             raise HTTPException(
#                 status_code=404,
#                 detail="Users not found"
#             )

#         users_list = []
#         for row in rows:
            
#             users_list.append({
#                 "id":row[0],
#                 "username":row[1],
#                 "business_type":row[2]
#             })
#         return {
#             "users" : users_list
#         }
        
#     except psycopg2.Error as e:
#         return {
#             "error": "Unable to create user",
#             "description": str(e)
#         }
#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()

# @app.post("/users")  
# def create_user(user: UserSchema):
#     conn = None
#     cursor = None
#     try:
#         conn = connect_db()
#         if conn is None:
#             raise HTTPException(
#             status_code=500,
#             detail="Database connection failed"
#         )
#         cursor = conn.cursor()
#         cursor.execute("""
#             INSERT INTO users (username, email, business_type)
#             VALUES
#                 (%s,%s,%s) RETURNING ID;
#             """,(user.username,user.email, user.business_type))
#         user_id = cursor.fetchone()
#         conn.commit()
#         if user_id is not None:
#             return {
#                 "message" : "User created successfully!!",
#                 "user_id": user_id[0]
#             }
        
#     except psycopg2.Error as e:
#         return {
#             "error": "Unable to create user",
#             "description": str(e)
#         }
#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()

# @app.get("/users/{user_id}/expenses")
# def get_user_expenses(user_id: int):
#     conn = None
#     cursor = None
#     try:
#         conn = connect_db()
#         if conn is None:
#             raise HTTPException(
#             status_code=500,
#             detail="Database connection failed"
#         )
#         cursor = conn.cursor()
#         cursor.execute("""
#             SELECT id,
#                 user_id,
#                 category,
#                 amount,
#                 description,
#                 expense_date,
#                 payment_method,
#                 created_at
#             FROM
#                 expenses
#             WHERE user_id = %s;
#             """,(user_id,))
#         rows = cursor.fetchall()
        
#         if not rows:
#             return {
#                 "message": "No Expense found"
#             }
#         expenses_list = []
#         for row in rows:
            
#             expenses_list.append({
#                 "id":row[0],
#                 "user_id":row[1],
#                 "category":row[2],
#                 "amount":row[3],
#                 "description": row[4],
#                 "expense_date":row[5],
#                 "payment_method":row[6],
#                 "created_at":row[7]
#             })
#         return {
#             "expenses" : expenses_list
#         }
#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()

# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     conn = None
#     cursor = None
#     try:
#         conn = connect_db()
#         if conn is None:
#             raise HTTPException(
#             status_code=500,
#             detail="Database connection failed"
#         )
#         cursor = conn.cursor()
#         cursor.execute("""
#             SELECT username, 
#                     email,
#                     business_type
#                 FROM users
#                 WHERE id = %s;
#             """,(user_id,))
#         row = cursor.fetchone()
#         if row is None:
#             raise HTTPException(
#             status_code=404,
#             detail="User not found"
#         )
#         return {
#             "username": row[0],
#             "email": row[1],
#             "business_type": row[2] 
#         }
        
#     except psycopg2.Error as e:
#         return {
#             "error": "Unable to find user",
#             "description": str(e)
#         }
#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()

# @app.put("/users/{user_id}")
# def update_user(user_id: int, user: UserSchema):
#     conn = None
#     cursor = None
#     try:
#         conn = connect_db()
#         if conn is None:
#             raise HTTPException(
#             status_code=500,
#             detail="Database connection failed"
#         )
#         cursor = conn.cursor()

        
#         cursor.execute("""
#             UPDATE users
#             set username = %s, 
#              email = %s,
#              business_type = %s
#             WHERE id = %s;
#             """,(user.username, user.email, user.business_type,user_id))
#         if cursor.rowcount == 0:
#             raise HTTPException(
#             status_code=404,
#             detail="User not found"
#         )
#         conn.commit()
#         return {
#             "message":"DATABASE UPDATED FOR THE USER",
#         }
        
#     except psycopg2.Error as e:
#         return {
#             "error": "Unable to update user",
#             "description": str(e)
#         }
#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()

# @app.delete("/users/{user_id}")
# def delete_user(user_id: int):
#     conn = None
#     cursor = None
#     try:
#         conn = connect_db()
#         if conn is None:
#             raise HTTPException(
#             status_code=500,
#             detail="Database connection failed"
#         )
#         cursor = conn.cursor()
#         cursor.execute("""
#             DELETE from users
#             WHERE id = %s;
#             """,(user_id,))
#         if cursor.rowcount == 0:
#             raise HTTPException(
#                 status_code=404,
#                 detail="User not found"
#             )
#         conn.commit()
#         return {
#             "message":"REMOVED USER FROM THE DATABASE",
#         }
        
#     except psycopg2.Error as e:
#         return {
#             "error": "Unable to delete user",
#             "description": str(e)
#         }
#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()


# # Clients
# @app.post("/clients")  
# def create_clients(client: ClientSchema):
#     conn = None
#     cursor = None
#     try:
#         conn = connect_db()
#         if conn is None:
#             raise HTTPException(
#             status_code=500,
#             detail="Database connection failed"
#         )
#         cursor = conn.cursor()
#         cursor.execute("""
#             INSERT INTO clients (user_id, client_name, email, phone)
#             VALUES
#                 (%s,%s,%s,%s) RETURNING ID;
#             """,(client.user_id,client.client_name,client.email, client.phone))
#         client_id = cursor.fetchone()
#         conn.commit()
#         if client_id is not None:
#             return {
#                 "message" : "Client created successfully!!",
#                 "client_id": client_id[0]
#             }
        
#     except psycopg2.Error as e:
#         return {
#             "error": "Unable to create client",
#             "description": str(e)
#         }
#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()


# @app.get("/clients/{client_id}")
# def get_client(client_id: int):
#     conn = None
#     cursor = None
#     try:
#         conn = connect_db()
#         if conn is None:
#             raise HTTPException(
#             status_code=500,
#             detail="Database connection failed"
#         )
#         cursor = conn.cursor()
#         cursor.execute("""
#             SELECT user_id, client_name, email, phone
#             FROM clients
#             WHERE id = %s
#             """,(client_id, ))
#         row = cursor.fetchone()
#         if row is not None:
#             return {
#                 "user_id":row[0],
#                 "client_name": row[1],
#                 "email": row[2],
#                 "phone":row[3]
#             }
        
#     except psycopg2.Error as e:
#         return {
#             "error": "Unable to find client",
#             "description": str(e)
#         }
#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()

# @app.put("/clients/{client_id}")
# def update_client(client_id: int, client: ClientSchema):
#     conn = None
#     cursor = None
#     try:
#         conn = connect_db()
#         if conn is None:
#             raise HTTPException(
#             status_code=500,
#             detail="Database connection failed"
#         )
#         cursor = conn.cursor()
#         cursor.execute("""
#             UPDATE clients
#             set 
#                 client_name = %s,       
#                 email = %s,
#                 phone = %s
#             WHERE id = %s
#             """,(client.client_name, client.email, client.phone, client_id))
#         conn.commit()
#         return {
#             "message":"Client updated from the database"
#         }
        
#     except psycopg2.Error as e:
#         return {
#             "error": "Unable to update client",
#             "description": str(e)
#         }
#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()


# @app.delete("/clients/{client_id}")
# def delete_client(client_id: int):
#     conn = None
#     cursor = None
#     try:
#         conn = connect_db()
#         if conn is None:
#             raise HTTPException(
#             status_code=500,
#             detail="Database connection failed"
#         )
#         cursor = conn.cursor()
#         cursor.execute("""
#             DELETE
#             FROM clients
#             WHERE id = %s
#             """,(client_id, ))
#         conn.commit()
#         return {
#             "message":"Client removed from the database"
#         }
        
#     except psycopg2.Error as e:
#         return {
#             "error": "Unable to delete client",
#             "description": str(e)
#         }
#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()


# # Invoices

# @app.post("/invoices")
# def create_invoice(invoice: InvoiceSchema):
#     conn = None
#     cursor = None
#     try:
#         conn = connect_db()
#         if conn is None:
#             raise HTTPException(
#             status_code=500,
#             detail="Database connection failed"
#         )
#         cursor = conn.cursor()
#         cursor.execute("""
#             INSERT INTO invoices
#             (
#                 user_id,
#                 client_id,
#                 amount,
#                 status,
#                 invoice_date
#                 due_date
#             )
#             VALUES
#             (%s, %s, %s, %s, %s, %s)
#             RETURNING ID;
#             """,(
#                 invoice.user_id, 
#                 invoice.client_id, 
#                 invoice.amount, 
#                 invoice.status, 
#                 invoice.invoice_date, 
#                 invoice.due_date
#             ))
#         invoice_id = cursor.fetchone()
#         conn.commit()

#         if invoice_id is None:
#             raise HTTPException(
#                 status_code=404,
#                 detail="No invoice id found"
#             )
#         return {
#             "message":"Added new invoice into the database",
#             "invoice_id": invoice_id[0]
#         }
        
#     except psycopg2.Error as e:
#         return {
#             "error": "Unable to create invoice",
#             "description": str(e)
#         }
#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()


# @app.get("/invoices")
# def get_invoices():
#     conn = None
#     cursor = None
#     try:
#         conn = connect_db()
#         if conn is None:
#             raise HTTPException(
#             status_code=500,
#             detail="Database connection failed"
#         )
#         cursor = conn.cursor()
#         cursor.execute("""
#             SELECT 
#                 id
#                 user_id,
#                 client_id,
#                 amount,
#                 status,
#                 invoice_date,
#                 due_date

#             FROM invoices;
#             """)
#         rows = cursor.fetchall()
#         if not rows:
#             raise HTTPException(
#                 status_code=404,
#                 detail="No invoices found"
#             )
        
#         invoices_list = []

#         for row in rows:
#             invoices_list.append({
#                 "id": row[0],
#                 "user_id": row[1],
#                 "client_id": row[2],
#                 "amount": row[3],
#                 "status": row[4],
#                 "invoice_date": row[5],
#                 "due_date": row[6]
#             })
#         return {
#             "invoices": invoices_list
#         }
        
#     except psycopg2.Error as e:
#         return {
#             "error": "Unable to find invoice",
#             "description": str(e)
#         }
#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()

# @app.post("/invoices/{invoice_id}")
# def get_invoice(invoice_id: int):
#     conn = None
#     cursor = None
#     try:
#         conn = connect_db()
#         if conn is None:
#             raise HTTPException(
#             status_code=500,
#             detail="Database connection failed"
#         )
#         cursor = conn.cursor()
#         cursor.execute("""
#             SELECT 
#                 id
#                 user_id,
#                 client_id,
#                 amount,
#                 status,
#                 invoice_date,
#                 due_date

#             FROM invoices
#             WHERE id = %s;
#             """, (invoice_id,))
#         row = cursor.fetchone()
#         if row is None:
#             raise HTTPException(
#                 status_code=404,
#                 detail="No invoice found"
#             )
#         return {
#             "id": row[0],
#             "user_id": row[1],
#             "client_id": row[2],
#             "amount": row[3],
#             "status": row[4],
#             "invoice_date": row[5],
#             "due_date": row[6]
#         }
        
#     except psycopg2.Error as e:
#         return {
#             "error": "Unable to find invoice",
#             "description": str(e)
#         }
#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()

# @app.put("/invoices/{invoice_id}")
# def update_invoice(invoice_id: int, invoice: InvoiceSchema):
#     conn = None
#     cursor = None
#     try:
#         conn = connect_db()
#         if conn is None:
#             raise HTTPException(
#             status_code=500,
#             detail="Database connection failed"
#         )
#         cursor = conn.cursor()
#         cursor.execute("""
#             UPDATE invoices
#             SET 
#                 user_id = %s,
#                 client_id = %s,
#                 amount = %s,
#                 status = %s,
#                 invoice_date = %s,
#                 due_date = %s
#             WHERE id = %s;
#             """, (
#                 invoice.user_id, 
#                 invoice.client_id, 
#                 invoice.amount, 
#                 invoice.status, 
#                 invoice.invoice_date, 
#                 invoice.due_date, 
#                 invoice_id
#             ))
#         conn.commit()

#         return {
#            "message":"Updated invoice from the database"
#         }
        
#     except psycopg2.Error as e:
#         return {
#             "error": "Unable to update invoice",
#             "description": str(e)
#         }
#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()

# @app.delete("/invoices/{invoice_id}")
# def delete_invoice(invoice_id: int):
#     conn = None
#     cursor = None
#     try:
#         conn = connect_db()
#         if conn is None:
#             raise HTTPException(
#             status_code=500,
#             detail="Database connection failed"
#         )
#         cursor = conn.cursor()
#         cursor.execute("""
#             DELETE FROM invoices
#             WHERE id = %s;
#             """, (
#                 invoice_id,
#             ))
#         conn.commit()

#         return {
#            "message":"Removed invoice from the database"
#         }
        
#     except psycopg2.Error as e:
#         return {
#             "error": "Unable to remove invoice",
#             "description": str(e)
#         }
#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()


# # Wallets

# @app.post("/wallets")
# def create_wallet(wallet: WalletSchema):
#     conn = None
#     cursor = None
#     try:
#         conn = connect_db()
#         if conn is None:
#             raise HTTPException(
#             status_code=500,
#             detail="Database connection failed"
#         )
#         cursor = conn.cursor()
#         cursor.execute("""
#             INSERT INTO wallets
#             (
#                 user_id,
#                 wallet_name,
#                 balance
#             )
#             VALUES
#             (%s, %s, %s)
#             RETURNING ID;
#             """,(
#                 wallet.user_id, 
#                 wallet.wallet_name, 
#                 wallet.balance
#             ))
#         wallet_id = cursor.fetchone()
#         conn.commit()

#         if wallet_id is None:
#             raise HTTPException(
#                 status_code=404,
#                 detail="No wallet found"
#             )
#         return {
#             "message":"Added new wallet into the database",
#             "wallet_id": wallet_id[0]
#         }
        
#     except psycopg2.Error as e:
#         return {
#             "error": "Unable to create wallet",
#             "description": str(e)
#         }
#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()


# @app.get("/wallets")
# def get_wallets():
#     conn = None
#     cursor = None
#     try:
#         conn = connect_db()
#         if conn is None:
#             raise HTTPException(
#             status_code=500,
#             detail="Database connection failed"
#         )
#         cursor = conn.cursor()
#         cursor.execute("""
#             SELECT 
#                 id
#                 user_id,
#                 wallet_name,
#                 balance
#             FROM wallets;
#             """)
#         rows = cursor.fetchall()
#         if not rows:
#             raise HTTPException(
#                 status_code=404,
#                 detail="No wallets found"
#             )
        
#         wallets_list = []

#         for row in rows:
#             wallets_list.append({
#                 "id": row[0],
#                 "user_id": row[1],
#                 "wallet_name": row[2],
#                 "balance": row[3]
            
#             })
#         return {
#             "wallets": wallets_list
#         }
        
#     except psycopg2.Error as e:
#         return {
#             "error": "Unable to find invoice",
#             "description": str(e)
#         }
#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()

# @app.post("/wallets/{wallet_id}")
# def get_wallet(wallet_id: int):
#     conn = None
#     cursor = None
#     try:
#         conn = connect_db()
#         if conn is None:
#             raise HTTPException(
#             status_code=500,
#             detail="Database connection failed"
#         )
#         cursor = conn.cursor()
#         cursor.execute("""
#             SELECT 
#                 user_id,
#                 wallet_name,
#                 balance
#             FROM wallets
#             WHERE id = %s;
#             """, (wallet_id,))
#         row = cursor.fetchone()
#         if row is None:
#             raise HTTPException(
#                 status_code=404,
#                 detail="No wallet found"
#             )
#         return {
#             "user_id": row[0],
#             "wallet_name": row[1],
#             "balance": row[2]
#         }
        
#     except psycopg2.Error as e:
#         return {
#             "error": "Unable to find wallet",
#             "description": str(e)
#         }
#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()

# @app.put("/wallets/{wallet_id}")
# def update_wallet(wallet_id: int, wallet: WalletSchema):
#     conn = None
#     cursor = None
#     try:
#         conn = connect_db()
#         if conn is None:
#             raise HTTPException(
#             status_code=500,
#             detail="Database connection failed"
#         )
#         cursor = conn.cursor()
#         cursor.execute("""
#             UPDATE wallets
#             SET 
#                 user_id = %s,
#                 wallet_name = %s,
#                 balance = %s
#             WHERE id = %s;
#             """, (
#                 wallet.user_id,
#                 wallet.wallet_name,
#                 wallet.balance,
#                 wallet_id
#             ))
#         conn.commit()

#         return {
#            "message":"Updated wallet from the database"
#         }
        
#     except psycopg2.Error as e:
#         return {
#             "error": "Unable to update wallet",
#             "description": str(e)
#         }
#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()

# @app.delete("/wallets/{wallet_id}")
# def delete_wallet(wallet_id: int):
#     conn = None
#     cursor = None
#     try:
#         conn = connect_db()
#         if conn is None:
#             raise HTTPException(
#             status_code=500,
#             detail="Database connection failed"
#         )
#         cursor = conn.cursor()
#         cursor.execute("""
#             DELETE FROM wallets
#             WHERE id = %s;
#             """, (
#                 wallet_id,
#             ))
#         conn.commit()

#         return {
#            "message":"Removed wallet from the database"
#         }
        
#     except psycopg2.Error as e:
#         return {
#             "error": "Unable to remove wallet",
#             "description": str(e)
#         }
#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()