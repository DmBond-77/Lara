from backend.db.database import engine, Base
from backend.db.models import Book  # Убедись, что модель импортируется

def init_db():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database and tables created.")

if __name__ == "__main__":
    init_db()
