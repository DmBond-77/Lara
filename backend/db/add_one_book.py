from backend.db.database import SessionLocal
from backend.db.models import Book  # Убедись, что модель импортирована

db = SessionLocal()

new_book = Book(
    title="The Great Gatsby",
    category="Classics",
    price=10.99,
    rating=5,
    image_url="https://example.com/gatsby.jpg",
    book_url="https://example.com/gatsby"
)

db.add(new_book)
db.commit()
db.close()

print("Book added successfully!")