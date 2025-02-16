import redis
import json
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db.models import Book
from backend.db.database import SessionLocal

router = APIRouter(prefix="/books", tags=["Books"])

# Подключение к Redis
redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

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
    sort_by: str | None = None,
    page: int = 1,
    limit: int = 10
):
    """Получаем список книг с кэшированием в Redis"""
    # Формируем ключ для кэша на основе параметров запроса
    cache_key = f"books:{category}:{max_price}:{min_price}:{title}:{sort_by}:{page}:{limit}"

    # Проверяем, есть ли кэшированный ответ
    cached_data = redis_client.get(cache_key)
    if cached_data:
        return json.loads(cached_data)

    # Если данных в кэше нет – получаем их из БД
    query = db.query(Book)
    
    if category:
        query = query.filter(Book.category == category)
    if max_price is not None:
        query = query.filter(Book.price <= max_price)
    if min_price is not None:
        query = query.filter(Book.price >= min_price)
    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))

    total_books = query.count()
    total_pages = (total_books + limit - 1) // limit

    if sort_by == "price_asc":
        query = query.order_by(Book.price.asc())
    elif sort_by == "price_desc":
        query = query.order_by(Book.price.desc())
    elif sort_by == "title":
        query = query.order_by(Book.title.asc())

    books = query.offset((page - 1) * limit).limit(limit).all()

    response_data = {
        "page": page,
        "limit": limit,
        "total_books": total_books,
        "total_pages": total_pages,
        "books": [book.__dict__ for book in books]
    }

    # Сохраняем результат в Redis на 60 секунд
    redis_client.setex(cache_key, 60, json.dumps(response_data, default=str))

    return response_data
