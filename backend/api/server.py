from fastapi import FastAPI
from backend.api.bak_books import router as books_router
import uvicorn
app = FastAPI()

app.include_router(books_router)  # Подключаем роуты для книг

@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в API!"}


if __name__ == "__main__":
    uvicorn.run("backend.api.server:app", reload=True)