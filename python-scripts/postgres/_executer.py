import argparse
import psycopg2

# Параметры подключения к базе данных
params = {
    'host': 'postgres',
    'database': 'mydatabase',
    'user': 'postgres',
    'password': 'postgres'
}

# Функция для выполнения SQL-запросов
def execute_query(query):
    # Подключение к базе данных
    conn = psycopg2.connect(**params)
    
    try:
        # Создание курсора
        cursor = conn.cursor()
        
        # Выполнение SQL-запроса
        cursor.execute(query)
        
        # Получение результатов запроса (если есть)
        result = cursor.fetchall()
        
        # Фиксация изменений в базе данных
        conn.commit()
        
        # Закрытие курсора и соединения
        cursor.close()
        conn.close()
        
        # Возврат результатов запроса
        return result
    
    except (Exception, psycopg2.DatabaseError) as error:
        # Обработка ошибок
        print("Ошибка при выполнении SQL-запроса:", error)
        conn.rollback()
        cursor.close()
        conn.close()

# Создание парсера аргументов командной строки
parser = argparse.ArgumentParser(description='Выполнение SQL-запроса к базе данных')
parser.add_argument('query', type=str, help='SQL-запрос для выполнения')

# Получение аргументов командной строки
args = parser.parse_args()

# Выполнение SQL-запроса
result = execute_query(args.query)

# Вывод результатов
for row in result:
    print(row)
