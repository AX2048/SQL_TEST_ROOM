import os
from sys import argv
import random
import string
from datetime import datetime
import base64
from faker import Faker
import psycopg2
from psycopg2 import sql


# Подготовка
fake = Faker('ru_RU')
cost = 100

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(
    host="postgres",
    database="outer_haven",
    user="postgres",
    password="postgres"
)


# Транслит
def latinizator(letter):
    legend = {' ': ' ', ',': ',', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': 'y', 'ы': 'y', 'ь': "'", 'э': 'e', 'ю': 'yu', 'я': 'ya', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo', 'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ъ': 'Y', 'Ы': 'Y', 'Ь': "'", 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya'}
    for i, j in legend.items():
        letter = letter.replace(i, j)
    return letter

# Собираем email из ФИО : Фамилия.ИО
def email_namer(name):
    latino_word = latinizator(name).lower()
    mail_hosts = ['gmail.com', 'yahoo.com', 'outlook.com', 'mail.ru', 'yandex.ru', 'ya.ru', 'vk.com', 'rambler.ru', 'bk.ru', 'inbox.ru']
    email = latino_word.split()[0].replace("'", "") + "." + latino_word.split()[1][0] + latino_word.split()[2][0] + "@" + random.choice(mail_hosts)
    return email

# Международный фонетический алфавит по первой букве ФИО
def ikato_namer(name):
    en_alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    en_ikato = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "Xray", "Yankee", "Zulu"]
    ikato = en_ikato[en_alfabet.index(latinizator(name).split()[0][0])] + " " + en_ikato[en_alfabet.index(latinizator(name).split()[1][0])] + " " + en_ikato[en_alfabet.index(latinizator(name).split()[2][0])]
    return ikato

# Random string
def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# Создаём пользователя
def create_user(name):
    user_public_name = name
    
    user_name_ru = user_public_name
    if len(user_public_name.split()) == 4: # убираем префиксы из имён тов. Faker'а
        user_name_ru = name.split()[1] + " " + name.split()[2] + " " + name.split()[3]
    
    user_name_en = latinizator(user_name_ru)
    user_b_date = fake.date()
    user_address = fake.address()
    user_email = email_namer(user_name_ru)
    user_job = fake.job()
    user_company = fake.company()
    user_ip = fake.ipv4_private()
    user_fio_ikato = ikato_namer(user_name_en)
    
    data_b64 = id_generator() + user_name_en + str(user_b_date)
    user_base64 = base64.b64encode(data_b64.encode()).decode()
    
    user_reg_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_description = fake.paragraph(nb_sentences=1)
    
    user_login = user_name_en.lower().split()[0].replace("'", "") + "." + user_name_en.lower().split()[1][0] + user_name_en.lower().split()[2][0] + "_" + user_base64[:8]
    user_phone_number = fake.phone_number()
    
    user = [user_public_name, user_name_ru, user_name_en, user_b_date, user_address, user_email, user_job, user_company, user_ip, user_fio_ikato, user_base64, user_reg_date, user_description, user_login, user_phone_number]
    return user


#for _ in range(cost):
#    print(create_user(fake.name()))

# user_public_name 1
# user_name_ru 2
# user_name_en 3 
# user_b_date 4
# user_address 5
# user_email 6
# user_job 7
# user_company 8
# user_ip 9
# user_fio_ikato 10
# user_base64 11
# user_reg_date 12
# user_description 13
# user_login 14
# user_phone_number 15

try:
    # Создание объекта "курсор" для выполнения SQL-запросов
    cursor = conn.cursor()

    for _ in range(cost):
        
        query = """
        INSERT INTO fake_names (user_public_name, user_name_ru, user_name_en, user_b_date, user_address, user_email, user_job, user_company, user_ip, user_fio_ikato, user_base64, user_reg_date, user_description, user_login, user_phone_number)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        user = create_user(fake.name())
        values = (user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8], user[9], user[10], user[11], user[12], user[13], user[14])
        cursor.execute(query, values)

    # Подтверждение изменений
    conn.commit()
    print("Записи успешно добавлены в таблицу 'fake_names'")

except (Exception, psycopg2.Error) as error:
    print("Ошибка при добавлении записей:", error)

finally:
    # Закрытие курсора и соединения с базой данных
    if cursor:
        cursor.close()
    if conn:
        conn.close()
