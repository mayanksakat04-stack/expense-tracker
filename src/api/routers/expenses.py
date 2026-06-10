from fastapi import APIRouter
from fastapi import Depends
from ..db_connection import get_db
from psycopg2.extras import RealDictCursor
from ...models.schemas import ExpenseSchema
import psycopg2
from fastapi import HTTPException
router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)

@router.get("/")
def get_expenses(conn = Depends(get_db)):
    try:
        cursor = conn.cursor(
            cursor_factory=RealDictCursor
        )
        cursor.execute("""
            SELECT id,
                user_id,
                category,
                amount,
                description,
                expense_date,
                payment_method,
                created_at
            FROM
                expenses
            """)
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(
                status_code=404,
                detail="No expenses found"
            )
    except psycopg2.Error as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    return {
        "expenses" : rows
    }

@router.get("/{expense_id}")
def get_expense(expense_id: int, conn = Depends(get_db)):
    try:
        cursor = conn.cursor(
            cursor_factory=RealDictCursor
        )
        cursor.execute("""
            SELECT id,
                user_id,
                category,
                amount,
                description,
                expense_date,
                payment_method,
                created_at
            FROM
                expenses
            WHERE id = %s
            """, (expense_id,))
        row = cursor.fetchone()
        if row is None:
            raise HTTPException(
                status_code=404,
                detail="No expense found"
            )
    except psycopg2.Error as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    return row

@router.post("/")
def create_expense(expense: ExpenseSchema, conn = Depends(get_db)):
    try:
        cursor = conn.cursor(
            cursor_factory=RealDictCursor
        )
        cursor.execute("""
            INSERT INTO expenses (
                    user_id,
                    category,
                    amount,
                    description,
                    payment_method
                )
            VALUES
                (%s,%s,%s,%s,%s) RETURNING ID;
            """,(expense.user_id, 
                expense.category, 
                expense.amount, 
                expense.description, 
                expense.payment_method))
        expense_id = cursor.fetchone()
        conn.commit()
        if expense_id is not None:
            return {
                "message" : "Expense created successfully!!",
                "expense_id": expense_id["id"]
            }
    except psycopg2.Error as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@router.put("/{expense_id}")
def update_expense(expense_id: int,expense: ExpenseSchema, conn = Depends(get_db)):
    try:
        cursor = conn.cursor(
            cursor_factory=RealDictCursor
        )
        cursor.execute("""
            UPDATE expenses
            set 
                user_id = %s,     
                category = %s,
                amount = %s,
                description = %s,
                payment_method = %s
            WHERE id = %s;
            """,(expense.user_id, expense.category, expense.amount, expense.description, expense.payment_method,expense_id))
        if cursor.rowcount == 0:
                raise HTTPException(
                status_code=404,
                detail="Expense not found"
            )
        conn.commit()
        return {
                "message":"DATABASE UPDATED FOR THE EXPENSE",
        }
    
    except psycopg2.Error as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@router.delete("/{expense_id}")
def delete_expense(expense_id: int, conn = Depends(get_db)):
    try:
        cursor = conn.cursor(
            cursor_factory=RealDictCursor
        )
        cursor.execute("""
            DELETE from expenses
            WHERE id = %s;
            """,(expense_id,))
        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Expense not found"
            )
        conn.commit()
        return {
            "message":"REMOVED EXPENSE FROM THE DATABASE",
        }
        
    except psycopg2.Error as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )