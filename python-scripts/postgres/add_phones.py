import random
import psycopg2

# Количество записей
number_of_phones = 50

# Параметры подключения к базе данных
params = {
    "host": "postgres",
    "database": "mydatabase",
    "user": "postgres",
    "password": "postgres"
}

# Список моделей телефонов
phone_models = [
    "IPhone 14",
    "Infinx note 12 VIP",
    "Nokia 3310",
    "IPhone 8 plus",
    "Sony Xperia Ultra"
]

# Установка соединения с базой данных
conn = psycopg2.connect(**params)
cursor = conn.cursor()

# Заполнение таблицы phones
for i in range(number_of_phones):
    phone_model = random.choice(phone_models)
    user_id = random.randint(300, 350)  # Пример ID пользователя, замените на свою логику

    # Формирование SQL-запроса на вставку
    query = "INSERT INTO phones (phone_model, user_id) VALUES (%s, %s)"
    values = (phone_model, user_id)

    # Выполнение SQL-запроса
    cursor.execute(query, values)

# Фиксация изменений и закрытие соединения с базой данных
conn.commit()
cursor.close()
conn.close()
