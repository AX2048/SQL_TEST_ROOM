from faker import Faker
import random
import string


fake = Faker('ru_RU')

cost = 2

def id_generator(size=16, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

for _ in range(cost):
    print("---")
    print(fake.name())
    print(fake.ipv4_private())
    print(fake.address())
    print(fake.paragraph(nb_sentences=1))
    print(fake.date_of_birth())
    print(fake.date())
    print(id_generator())
