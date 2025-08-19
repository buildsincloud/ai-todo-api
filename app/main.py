from fastapi import FastAPI
from app.api.v1.endpoints import todos

app = FastAPI(title="AI TODO API", version="0.2.0")
app.include_router(todos.router, prefix="/api/v1/todos", tags=["todos"])

@app.get("/health")
def health():
    return {"status": "ok"}
