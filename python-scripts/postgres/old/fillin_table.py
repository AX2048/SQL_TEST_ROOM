import psycopg2
from psycopg2 import sql
from datetime import datetime
import random
import hashlib

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(
    host="postgres",
    database="outer_haven",
    user="postgres",
    password="postgres"
)

# Заполнение таблицы "names"
names_data = [
    {"name": "Big Boss"},
    {"name": "Ahab"},
    {"name": "Ishmael"},
    {"name": "EVA"},
    {"name": "Quiet"},
    {"name": "Shalashaka"},
    {"name": "Paz"},
    {"name": "Dr. Strangelove"},
    {"name": "Benedict Miller"},
    {"name": "Eli"}
]

try:
    # Создание объекта "курсор" для выполнения SQL-запросов
    cursor = conn.cursor()

    for name_data in names_data:
        # Генерация случайного 6-значного числа
        number = random.randint(100000, 999999)

        # Генерация хеша имени и числа
        name_number_str = f"{name_data['name']}{number}"
        key = hashlib.sha256(name_number_str.encode()).hexdigest()

        # Получение текущей даты и времени
        created_at = datetime.now()

        # Создание SQL-запроса для вставки записи
        insert_query = sql.SQL("""
            INSERT INTO names (name, created_at, number, description, key)
            VALUES (%s, %s, %s, %s, %s)
        """)

        # Выполнение SQL-запроса для вставки записи
        cursor.execute(insert_query, (name_data['name'], created_at, number, "Описание", key))

    # Подтверждение изменений
    conn.commit()

    print("Записи успешно добавлены в таблицу 'names'")

except (Exception, psycopg2.Error) as error:
    print("Ошибка при добавлении записей:", error)

finally:
    # Закрытие курсора и соединения с базой данных
    if cursor:
        cursor.close()
    if conn:
        conn.close()
