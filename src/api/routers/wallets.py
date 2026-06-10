from fastapi import APIRouter

router = APIRouter(
    prefix="/wallets",
    tags=["Wallets"]
)

@router.post("/")
def create_wallet():
    pass

@router.get("/{wallet_id}")
def get_wallet():
    pass

@router.put("/{wallet_id}")
def update_wallet():
    pass

@router.delete("/{wallet_id}")
def delete_wallet():
    pass