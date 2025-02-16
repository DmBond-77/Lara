import sys
import os
from sqlalchemy import text
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.db.database import SessionLocal


try:
    db = SessionLocal()
    db.execute(text("SELECT 1"))  # Проверяем соединение
    print("Подключение к базе данных успешно!")
except Exception as e:
    print(f"Ошибка подключения: {e}")
finally:
    db.close()

