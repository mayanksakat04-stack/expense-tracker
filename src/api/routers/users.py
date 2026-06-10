from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/")
def create_user():
    pass

@router.get("/{user_id}")
def get_user():
    pass

@router.put("/{user_id}")
def update_user():
    pass

@router.delete("/{user_id}")
def delete_user():
    pass