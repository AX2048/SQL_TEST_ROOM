from faker import Faker

fake = Faker('ru_RU')

cost = 2

for _ in range(cost):
  print("---")
  print(fake.name())
  print(fake.ipv4_private())
  print(fake.address())
  print(fake.paragraph(nb_sentences=1))
  print(fake.date_of_birth())
  print(fake.date())

