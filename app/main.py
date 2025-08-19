from fastapi import FastAPI
from app.api.v1.endpoints import todos, ai

app = FastAPI(title="AI TODO API", version="0.3.0")
app.include_router(todos.router, prefix="/api/v1/todos", tags=["todos"])
app.include_router(ai.router, prefix="/api/v1/ai", tags=["ai"])

@app.get("/health")
def health():
    return {"status": "ok"}
