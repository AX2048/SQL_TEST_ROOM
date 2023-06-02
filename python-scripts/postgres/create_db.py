import psycopg2
#from psycopg2 import extensions

# Подключение к базе данных PostgreSQL (предварительно созданной базе данных "postgres")
conn = psycopg2.connect(
    host="postgres",
    database="postgres",
    user="postgres",
    password="postgres"
)

# Отключение блокировки транзакций
#conn.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)

# Создание базы данных "outer_haven"
create_db_query = "CREATE DATABASE outer_haven"

try:
    # Создание объекта "курсор" для выполнения SQL-запросов
    cursor = conn.cursor()

    # Выполнение запроса создания базы данных
    cursor.execute(create_db_query)

    # Подтверждение изменений
    conn.commit()

    print("База данных 'outer_haven' успешно создана")

except (Exception, psycopg2.Error) as error:
    print("Ошибка при создании базы данных:", error)

finally:
    # Закрытие курсора и соединения с базой данных "postgres"
    if cursor:
        cursor.close()
    if conn:
        conn.close()
