import psycopg2

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(
    host="postgres",
    database="outer_haven",
    user="postgres",
    password="postgres"
)

# Создание таблицы "names"
create_table_query = """
    CREATE TABLE names (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        created_at TIMESTAMP,
        number INTEGER,
        description TEXT,
        key VARCHAR(150)
    )
"""

try:
    # Создание объекта "курсор" для выполнения SQL-запросов
    cursor = conn.cursor()

    # Выполнение запроса создания таблицы
    cursor.execute(create_table_query)

    # Подтверждение изменений
    conn.commit()

    print("Таблица 'names' успешно создана")

except (Exception, psycopg2.Error) as error:
    print("Ошибка при создании таблицы:", error)

finally:
    # Закрытие курсора и соединения с базой данных
    if cursor:
        cursor.close()
    if conn:
        conn.close()
