import psycopg2

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(
    host="postgres",
    database="outer_haven",
    user="postgres",
    password="postgres"
)

# Создание таблицы "fake_names"
create_table_query = """
    CREATE TABLE fake_names (
        id SERIAL PRIMARY KEY,
        user_public_name VARCHAR(100),
        user_name_ru VARCHAR(100),
        user_name_en VARCHAR(100),
        user_b_date VARCHAR(100),
        user_address VARCHAR(250),
        user_email VARCHAR(50),
        user_job VARCHAR(50),
        user_company VARCHAR(100),
        user_ip VARCHAR(50),
        user_fio_ikato VARCHAR(100),
        user_base64 TEXT,
        user_reg_date TIMESTAMP,
        user_description TEXT,
        user_login VARCHAR(50),
        user_phone_number VARCHAR(50)
    )
"""

# user_public_name
# user_name_ru
# user_name_en
# user_b_date
# user_address
# user_email
# user_job
# user_ip
# user_fio_ikato
# user_base64
# user_reg_date
# user_description
# user_login
# user_phone_number

try:
    # Создание объекта "курсор" для выполнения SQL-запросов
    cursor = conn.cursor()

    # Выполнение запроса создания таблицы
    cursor.execute(create_table_query)

    # Подтверждение изменений
    conn.commit()

    print("Таблица fake_names успешно создана")

except (Exception, psycopg2.Error) as error:
    print("Ошибка при создании таблицы:", error)

finally:
    # Закрытие курсора и соединения с базой данных
    if cursor:
        cursor.close()
    if conn:
        conn.close()
