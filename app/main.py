from fastapi import FastAPI
from typing import Optional

# FastAPI 인스턴스 생성
app = FastAPI(
    title="My First FastAPI App",
    description="This is a first FastAPI tutorial",
    version="1.0.0"
)

# 기본 라우트
@app.get("/")
async def root():
    return {"message": "Hello FastAPI!"}

# 경로 매개변수 사용
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}