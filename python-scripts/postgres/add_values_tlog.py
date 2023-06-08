import random
from datetime import datetime, timedelta
import psycopg2

# Параметры подключения к базе данных PostgreSQL
host = "postgres"
database = "outer_haven"
user = "postgres"
password = "postgres"

# Список возможных значений для полей action и error_message
actions = ['login', 'act_x', 'act_y']
error_messages = ['err_x', 'err_y', 'some_error', None]

# Список возможных значений для поля user
users = ['ivanov', 'smith', 'johnson', 'brown']

# Установка соединения с базой данных
conn = psycopg2.connect(host=host, database=database, user=user, password=password)
cur = conn.cursor()

# Создание 50 записей
for _ in range(50):
    action = random.choice(actions)
    error_message = random.choice(error_messages)
    user = random.choice(users)
    dtm = datetime.now() - timedelta(days=random.randint(0, 30))

    # Вставка записи в таблицу t_log
    cur.execute("INSERT INTO t_log (action, error_message, \"user\", dtm) VALUES (%s, %s, %s, %s)",
                (action, error_message, user, dtm))

# Фиксация изменений и закрытие соединения
conn.commit()
cur.close()
conn.close()

print("50 записей было успешно создано в таблице t_log.")
