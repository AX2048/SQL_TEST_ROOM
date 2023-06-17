import random
from datetime import datetime, timedelta
import psycopg2
import base64
from faker import Faker

# Количество пользователей
number_of_users = 100

# INIT
fake = Faker()

# Параметры подключения к базе данных PostgreSQL
host = "postgres"
database = "outer_haven"
user = "postgres"
password = "postgres"

# Список возможных значений для полей action и error_message
actions = ['login', 'logout', 'edit', 'add', 'delete', 'move', 'rename']
error_messages = ['log_err', 'timeout_err', 'some_err', None]

# Список возможных значений для поля user
users = ['ivanov', 'smith', 'johnson', 'brown', 'John', 'Mary', 'Alex', 'Kate', 'Mike', 'Lisa']

# Установка соединения с базой данных
conn = psycopg2.connect(host=host, database=database, user=user, password=password)
cur = conn.cursor()

# Создание 50 записей
for _ in range(number_of_users):
    action = random.choice(actions)
    error_message = random.choice(error_messages)
    username = fake.name().lower()
    #username = random.choice(users).lower()
    dtm = datetime.now() - timedelta(days=random.randint(0, 30))

    # Вставка записи в таблицу t_log
    cur.execute("INSERT INTO t_log (action, error_message, username, dtm) VALUES (%s, %s, %s, %s)",
                (action, error_message, username, dtm))

# Фиксация изменений и закрытие соединения
conn.commit()
cur.close()
conn.close()

print(f"{number_of_users} записей было успешно создано в таблице t_log.")
