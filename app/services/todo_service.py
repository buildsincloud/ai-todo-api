from datetime import datetime, timezone
from typing import List, Dict
from app.schemas.todo import TodoCreate, TodoRead

class TodoService:
    def __init__(self):
        self._items: Dict[int, TodoRead] = {}
        self._id = 0

    def create(self, payload: TodoCreate) -> TodoRead:
        self._id += 1
        item = TodoRead(id=self._id, created_at=datetime.now(timezone.utc), **payload.model_dump())
        self._items[item.id] = item
        return item
    
    def list(self) -> List[TodoRead]:
        return list(self._items.values())