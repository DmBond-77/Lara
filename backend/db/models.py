from backend.db.database import Base
from sqlalchemy import Column, Integer, String, Numeric, Text

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    category = Column(String(100))
    price = Column(Numeric(10, 2))
    rating = Column(Integer)
    image_url = Column(Text)
    book_url = Column(Text)
