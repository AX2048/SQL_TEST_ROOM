import psycopg2
import random

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(
    host="postgres",
    database="outer_haven",
    user="postgres",
    password="postgres"
)

# Список возможных значений для поля "role"
roles = ["admin", "moder", "user"]

try:
    # Создание объекта "курсор" для выполнения SQL-запросов
    cursor = conn.cursor()

    # Получение всех записей из таблицы "names"
    select_query = "SELECT id FROM names"
    cursor.execute(select_query)
    records = cursor.fetchall()

    for record in records:
        # Генерация случайного значения из списка "roles"
        role = random.choice(roles)

        # Обновление поля "role" для текущей записи
        update_query = f"UPDATE names SET role = '{role}' WHERE id = {record[0]}"
        cursor.execute(update_query)

    # Подтверждение изменений
    conn.commit()

    print("Поле 'role' успешно заполнено")

except (Exception, psycopg2.Error) as error:
    print("Ошибка при заполнении поля 'role':", error)

finally:
    # Закрытие курсора и соединения с базой данных
    if cursor:
        cursor.close()
    if conn:
        conn.close()
