import mysql.connector
import random
from datetime import datetime, timedelta

mydb = mysql.connector.connect(
    host="mysql",
    user="root",
    password="example",
    database="mydatabase"
)

mycursor = mydb.cursor()

# создание таблицы пользователей
mycursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")

# заполнение таблицы пользователей данными
user_names = ['Paz', 'Anna', 'Tom', 'Kate', 'Mike', 'Julia']
users = []
for name in user_names:
    user = (name,)
    users.append(user)

user_sql = "INSERT INTO users (name) VALUES (%s)"
mycursor.executemany(user_sql, users)
mydb.commit()

# создание таблицы подписчиков
mycursor.execute("CREATE TABLE IF NOT EXISTS subscribers (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, subscriber_user_id INT)")

# заполнение таблицы подписчиков данными
subscribers = []
for i in range(1, 7):
    for j in range(1, 7):
        if i != j:
            subscriber = (i, j)
            subscribers.append(subscriber)

subscriber_sql = "INSERT INTO subscribers (user_id, subscriber_user_id) VALUES (%s, %s)"
mycursor.executemany(subscriber_sql, subscribers)
mydb.commit()

# создание таблицы комментариев
mycursor.execute("CREATE TABLE IF NOT EXISTS comments (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, text TEXT, created DATETIME)")

# заполнение таблицы комментариев данными
comments = []
for i in range(1, 37):
    user_id = random.randint(1, 6)
    text = 'Comment {}'.format(i)
    created = datetime.now() - timedelta(days=random.randint(0, 365))
    comment = (user_id, text, created)
    comments.append(comment)

comment_sql = "INSERT INTO comments (user_id, text, created) VALUES (%s, %s, %s)"
mycursor.executemany(comment_sql, comments)
mydb.commit()

print("Данные успешно добавлены в таблицы!")
