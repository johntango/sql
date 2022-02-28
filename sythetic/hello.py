from faker import Faker
fake = Faker()

print(fake.first_name(), fake.last_name())
print(fake.job())
