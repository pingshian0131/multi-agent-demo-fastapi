from fastapi import FastAPI, HTTPException, status
from typing import List, Dict
from pydantic import BaseModel, Field

app = FastAPI(title="To-Do List API")

# In-memory database
todos: List[Dict] = []
counter = 0

# Pydantic models
class TodoCreate(BaseModel):
    task: str = Field(..., min_length=1, max_length=100)

class TodoResponse(BaseModel):
    id: int
    task: str

class DeleteResponse(BaseModel):
    status: str
    message: str

@app.get("/todos", response_model=List[TodoResponse])
async def get_todos():
    return todos

@app.post("/todos", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoCreate):
    global counter
    counter += 1
    new_todo = {"id": counter, "task": todo.task}
    todos.append(new_todo)
    return new_todo

@app.delete("/todos/{item_id}", response_model=DeleteResponse)
async def delete_todo(item_id: int):
    for i, todo in enumerate(todos):
        if todo["id"] == item_id:
            todos.pop(i)
            return {"status": "success", "message": f"To-Do item with id {item_id} deleted"}
    raise HTTPException(status_code=404, detail=f"To-Do item with id {item_id} not found")
