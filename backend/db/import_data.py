import csv
import os
from backend.db.database import SessionLocal
from backend.db.models import Book

def import_csv_to_db(csv_file: str):
    session = SessionLocal()
    print(f"Opening file: {csv_file}")
    
    try:
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)  # Отладочный вывод строки CSV
                
                rating = int(row["Rating"]) if row["Rating"].isdigit() else None
                book = Book(
                    title=row["Title"],
                    price=float(row["Price"]),
                    rating=rating,
                    image_url=row["Image URL"],
                    book_url=row["Book URL"],
                    category=row["Category"]
                )
                print(f"Inserting: {book.title}, {book.price}, {book.rating}, {book.image_url}, {book.book_url}, {book.category}")
                session.add(book)
        
        session.commit()
        print("Data imported successfully.")
    except Exception as e:
        session.rollback()
        print("Error:", e)
    finally:
        session.close()

if __name__ == "__main__":
    CSV_FILE_PATH = r"E:\My_documents\Lara\project\selenium\books.csv"
    if not os.path.exists(CSV_FILE_PATH):
        print(f"Error: CSV file not found at {CSV_FILE_PATH}")
    else:
        import_csv_to_db(CSV_FILE_PATH)