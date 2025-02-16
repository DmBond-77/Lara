from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from backend.db.models import Book
from backend.db.database import SessionLocal

router = APIRouter(prefix="/books", tags=["Books"])

# Функция для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_books(
    db: Session = Depends(get_db),
    category: str | None = None,
    max_price: float | None = None,
    min_price: float | None = None,
    title: str | None = None,
    sort_by: str | None = None,  # Сортировка
    page: int = 1,  # Пагинация (по умолчанию первая страница)
    limit: int = 10  # Сколько книг на странице
):
    """Получаем список всех книг с фильтрацией, сортировкой и пагинацией"""
    if page < 1:
        page = 1
    if limit < 1:
        limit = 10

    query = db.query(Book)
    
    if category:
        query = query.filter(Book.category == category)
    if max_price is not None:
        query = query.filter(Book.price <= max_price)
    if min_price is not None:
        query = query.filter(Book.price >= min_price)
    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))

    # Подсчет общего количества книг после фильтрации
    total_books = query.count()
    total_pages = (total_books + limit - 1) // limit  # Вычисляем количество страниц

    # Сортировка
    if sort_by == "price_asc":
        query = query.order_by(Book.price.asc())
    elif sort_by == "price_desc":
        query = query.order_by(Book.price.desc())
    elif sort_by == "title":
        query = query.order_by(Book.title.asc())

    # Пагинация
    offset = (page - 1) * limit
    books = query.offset(offset).limit(limit).all()

    return {
        "page": page,
        "limit": limit,
        "total_books": total_books,
        "total_pages": total_pages,
        "books": books
    }
