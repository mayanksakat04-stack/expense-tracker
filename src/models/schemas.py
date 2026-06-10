from pydantic import BaseModel

class ExpenseSchema(BaseModel):
    user_id: int
    category: str
    amount : int
    description: str
    payment_method: str

class UserSchema(BaseModel):
    username: str
    email: str
    business_type: str

class ClientSchema(BaseModel):
    user_id: int
    client_name: str
    email: str
    phone: str

class InvoiceSchema(BaseModel):
    user_id : int
    client_id: int
    amount: int
    status: str
    invoice_date: str
    due_date: str

class WalletSchema(BaseModel):
    user_id: int
    wallet_name: str
    balance: int