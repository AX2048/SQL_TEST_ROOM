import os
from sys import argv
import random
from faker import Faker


# Подготовка
fake = Faker('ru_RU')
cost = 2000

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


# Использование
for _ in range(cost):
    name = fake.name()
    print(f"Name :: {name} // {len(name.split())}")
    
    if len(name.split()) == 4: # убираем префиксы из имён тов. Faker'а
        name = name.split()[1] + " " + name.split()[2] + " " + name.split()[3]
    
    print(f"| ikato = {ikato_namer(name)} | Имя :: {name} | Name :: {latinizator(name)} | date :: {fake.date()} | Job :: {fake.job()} | Email :: {email_namer(name)} | Адрес :: {fake.address()} | IP :: {fake.ipv4_private()} |")
