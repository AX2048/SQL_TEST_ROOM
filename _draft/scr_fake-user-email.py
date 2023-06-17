import os
from sys import argv
import random
from faker import Faker

fake = Faker('ru_RU')

cost = 100

def latinizator(letter):
    legend = {' ': ' ', ',': ',', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': 'y', 'ы': 'y', 'ь': "'", 'э': 'e', 'ю': 'yu', 'я': 'ya', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo', 'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ъ': 'Y', 'Ы': 'Y', 'Ь': "'", 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya'}
    for i, j in legend.items():
        letter = letter.replace(i, j)
    return letter

def email_namer(name):
    latino_word = latinizator(name).lower()
    mail_hosts = ['gmail.com', 'yahoo.com', 'outlook.com', 'mail.ru', 'yandex.ru', 'ya.ru', 'vk.com', 'rambler.ru', 'bk.ru', 'inbox.ru']
    email = latino_word.split()[0].replace("'", "") + "." + latino_word.split()[1][0] + latino_word.split()[2][0] + "@" + random.choice(mail_hosts)
    return(email)

for _ in range(cost):
    name = fake.name()
    print(f"| Имя :: {name} | Name :: {latinizator(name)} | Email :: {email_namer(name)} |")