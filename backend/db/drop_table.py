from backend.db.database import Base, engine
from backend.db.models import Book

# Удаляем таблицу books
Book.__table__.drop(engine, checkfirst=True)
print("Таблица books удалена!")
