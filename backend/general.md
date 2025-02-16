1. Фильтрацию и поиск – возможность искать книги по категории, цене, названию.
2. Авторизацию – ограничение доступа к API для неавторизованных пользователей.
3. Создание, обновление и удаление книг – API должен позволять управлять данными.
4. Swagger-документацию – более детальное описание API.

Теперь можно делать запросы, например:

Все книги: GET /books/
Книги в категории "Fiction": GET /books/?category=Fiction
Книги дешевле 20: GET /books/?max_price=20
Книги дороже 10: GET /books/?min_price=10
Книги, содержащие "Python" в названии: GET /books/?title=Python
/books/?category=Fiction&min_price=10&max_price=50&sort_by=price_asc
/books/?title=Python&sort_by=title
Да, в твоем коде уже есть фильтрация по:
✅ Категории (category=Fiction)
✅ Минимальной цене (min_price=10)
✅ Максимальной цене (max_price=50)
✅ Частичному совпадению названия (title=Python)

Я добавил:
✅ Сортировку (sort_by=price_asc, sort_by=price_desc, sort_by=title)
