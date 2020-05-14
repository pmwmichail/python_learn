# Universitet project
Создаем базу данных и заполняем ее

create_db.py -- скрипт для создания бд (если не создана),
и всех ее таблиц

models.py -- скрипт содержащий сами модели ORM
SQLAlchemy

test.py -- файлик для пороверки

univerdb -- база sqllite3

insert_data.sql -- запросы для заполнения БД

### Как работать
1. Если нет базы, то запустить createdb.py и 
заполнить данными из insert_data.sql
2. Запустить test.py