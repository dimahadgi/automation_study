import random


from faker import Faker

fake = Faker()


def generate_fake_data():
    fake_data = {
        "email": fake.email(),
        "email2": fake.email(),
        "first_and_last_name": fake.name(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "name_prefix": fake.prefix(),
        "cert_name": fake.company(),
        "cert_name2": fake.company(),
        "city": fake.city(),
        "country": fake.country(),
        "street_name": fake.street_name(),
        "random_phrase": fake.catch_phrase(),
        "random_phrase2": fake.catch_phrase(),
        "random_number": fake.ean(length=13)
    }
    return fake_data


def gen_date():
    expiration_date = "{}-{}-{}T15:15:10.440Z".format(
        random.randint(2017, 2023),
        random.choice(["%.2d" % i for i in range(1, 12)]),
        random.choice(["%.2d" % i for i in range(1, 25)]))
    return expiration_date

