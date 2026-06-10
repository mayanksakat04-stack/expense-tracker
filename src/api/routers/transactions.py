from fastapi import APIRouter

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

@router.post("/")
def create_transaction():
    pass

@router.get("/{transaction_id}")
def get_transaction():
    pass

@router.put("/{transaction_id}")
def update_transaction():
    pass

@router.delete("/{transaction_id}")
def delete_transaction():
    pass