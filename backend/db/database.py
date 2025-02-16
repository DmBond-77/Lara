# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "postgresql://postgres:123456@localhost:5432/books_db"

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()



from sqlalchemy import create_engine, Column, Integer, String, Numeric, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging

# Логирование SQL-запросов (для отладки)
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

# Укажи правильный `DATABASE_URL`
DATABASE_URL = "postgresql://postgres:123456@localhost:5432/books_db"

# Создание движка и сессии
engine = create_engine(DATABASE_URL, echo=True)  # echo=True для вывода SQL-запросов
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()
