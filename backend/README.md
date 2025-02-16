# Backend Project Setup

## Описание файлов

- `database.py` – устанавливает подключение к PostgreSQL через SQLAlchemy.
- `models.py` – определяет модель `Book` с полями: `id`, `title`, `category`, `price`, `rating`, `image_url`, `book_url`.
- `init_db.py` – создает таблицы в базе данных, используя SQLAlchemy.
- `drop_table.py` – удаляет таблицу `books`, если она существует.
- `import_data.py` – загружает данные книг из CSV или другого источника в базу данных.
- `add_one_book.py` – добавляет одну книгу в базу данных.
- `test_db.py` – тестирует соединение с базой данных и выполняет пробные запросы.
- `server.py` – запускает API-сервер для взаимодействия с базой данных (например, через FastAPI).

## Порядок запуска

1. **Удалить таблицу (если нужно)**

   ```bash
   python backend/drop_table.py
   py -m backend.db.drop_table

   ```

2. **Создать таблицы**

   ```bash
   python backend/init_db.py
   py -m backend.db.init_db

   ```

3. **Импортировать данные**

   ```bash
   python backend/import_data.py
   py -m backend.db.import_data

   ```

4. **(Опционально) Добавить одну книгу вручную**

   ```bash
   python backend/add_one_book.py
   py -m backend.db.add_one_book
   ```

5. **Запустить сервер API**

   ```bash
   python backend/server.py
   ```

6. **(Опционально) Протестировать базу**

   ```bash
   python backend/test_db.py
   py -m backend.tests.test_db
   ```
