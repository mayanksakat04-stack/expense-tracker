from fastapi import APIRouter

router = APIRouter(
    prefix="/invoices",
    tags=["Invoices"]
)

@router.post("/")
def create_invoice():
    pass

@router.get("/{invoice_id}")
def get_invoice():
    pass

@router.put("/{invoice_id}")
def update_invoice():
    pass

@router.delete("/{invoice_id}")
def delete_invoice():
    pass