
from ..database import get_connection
import psycopg2
from fastapi import HTTPException
def connect_db():
    try:
        return get_connection()
    except psycopg2.Error as e:
        print("Error in Database Connection: \n",e)
        return None
    

def get_db():
    conn = connect_db()
    if conn is None:
        raise HTTPException(
        status_code=500,
        detail="Database connection failed"
    )
    try:
        yield conn
    finally:
        conn.close()