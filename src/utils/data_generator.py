from faker import Faker

fake = Faker()


def generate_fake_data():
    fake_data = {
        "email": fake.email(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "cert_name": fake.company(),
        "city": fake.city(),
        "country": fake.country(),
        "street_name": fake.street_name(),
        "random_phrase": fake.catch_phrase()
    }
    return fake_data
