from fastapi import APIRouter, Depends
from typing import List
from app.schemas.todo import TodoCreate, TodoRead
from app.services.todo_service import TodoService

router = APIRouter()

_service = TodoService()
def get_service() -> TodoService:
    return _service

@router.post("/", response_model=TodoRead)
def create_todo(payload: TodoCreate, svc: TodoService = Depends(get_service)):
    return svc.create(payload)

@router.get("/", response_model=List[TodoRead])
def list_todos(svc: TodoService = Depends(get_service)):
    return svc.list()