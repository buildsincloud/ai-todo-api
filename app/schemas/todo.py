from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class TodoBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    due_at: Optional[str] = None

class TodoCreate(TodoBase):
    pass

class TodoRead(TodoBase):
    id: int
    created_at: datetime