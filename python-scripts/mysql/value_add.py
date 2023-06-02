import mysql.connector

# Подключение к БД
mydb = mysql.connector.connect(
    host="mysql",
    user="root",
    password="example",
    database="mydatabase"
)

# Создание курсора
mycursor = mydb.cursor()

# Вставка тестовой записи в таблицу
sql = "INSERT INTO users (name) VALUES ('Big Boss')"
mycursor.execute(sql)
# Подтверждение изменений
mydb.commit()

# Вывод ID новой записи
print("Record inserted, ID:", mycursor.lastrowid)
