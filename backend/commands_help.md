pip install -r requirements.txt `install the all packages`
E:\Program Files\PostgreSQL16\bin `the path to the env in windows`
git remote add origin https://github.com/DmBond-77/Lara.git

**command for postgresql**
https://hasura.io/blog/top-psql-commands-and-flags-you-need-to-know-postgresql

psql -U postgres -d books_db `connect to my db`
Use \q to quit.
List all databases - \l
Switch to another database - \c

```
\c <db-name>

// example
\c tutorials_db

```

List database tables - \dt
Describe a table - \d
List all schemas - \dn
List users and their roles - \du

SET client_encoding = 'UTF8'; `Change the client encoding in psql`

Get-Content E:\My_documents\Lara\project\selenium\books.csv `The command to check existing of books.csv `

**This runs a Python module as a script. It tells Python to locate the module inside a package and execute it.**

```
python -m backend.db.init_db

```

redis port 6379

Добавь путь навсегда (через графический интерфейс Windows):

Нажми Win + R, введи sysdm.cpl, нажми Enter.
Перейди в Дополнительно → Переменные среды.
Найди переменную Path, выбери Изменить.
Нажми Создать, введи путь к Redis (например, C:\Program Files\Redis).
Сохранить → Перезапустить PowerShell.
