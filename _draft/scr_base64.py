import base64

name = "example_name"
number = 12345

# Конвертировать имя и число в строку
data = name + str(number)

# Кодировать данные в Base64
encoded_data = base64.b64encode(data.encode()).decode()

print("Закодированное значение (Base64):", encoded_data)
