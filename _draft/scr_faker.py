from faker import Faker

fake = Faker('ru_RU')

cost = 10

for _ in range(cost):
  print(fake.name())
  print(fake.ipv4_private())
  print(fake.address())

