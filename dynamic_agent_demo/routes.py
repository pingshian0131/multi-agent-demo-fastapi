from fastapi import APIRouter
from models import AddRequest, UpdateItemRequest

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}

@router.post("/add")
async def add_numbers(request: AddRequest):
    return {"result": request.a + request.b}

@router.put("/item/{id}")
async def update_item(id: int, request: UpdateItemRequest):
    return {"status": "success", "message": f"Item {id} updated"}

@router.delete("/item/{id}")
async def delete_item(id: int):
    return {"status": "success", "message": f"Item {id} deleted"}