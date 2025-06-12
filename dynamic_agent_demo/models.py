
from pydantic import BaseModel
from typing import Optional

class AddRequest(BaseModel):
    a: int
    b: int

class UpdateItemRequest(BaseModel):
    title: str