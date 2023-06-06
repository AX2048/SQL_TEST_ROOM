import hashlib

name = "example_name"
number = 12345

# Конвертировать имя и число в строку
data = name + str(number)

# Создать объект SHA-256
sha256_hash = hashlib.sha256()

# Обновить хэш-объект с данными
sha256_hash.update(data.encode())

# Получить хэш в виде шестнадцатеричной строки
hash_value = sha256_hash.hexdigest()

print("Хэш значение (SHA-256):", hash_value)
