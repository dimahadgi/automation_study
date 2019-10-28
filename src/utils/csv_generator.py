import random
from faker import Faker
fake = Faker('en_CA')


TRADES = ["Boilermaker", "Carpenter", "Cement & Concrete Finisher", "Construction Office Manager", "Crane Operator",
          "Derrick Operator", "Deckhand", "Dredge Operator", "Driller", "Electrician", "Equipment Operator",
          "Elevator Mechanic", "Estimator", "Fencer/Fence Erector", "Foreman", "Framer", "Glazier",
          "Heavy Equipment Operator", "HVAC Tech", "Insulation Worker", "Iron-worker", "Joiner", "Laborer",
          "Landscaper", "Leverman", "Mason", "Mill Worker", "Millwright", "Oiler", "Painter / Plasterer",
          "Pile Driver Operator", "Plumber", "Pipefitter", "Rigger", "Roofer", "Steamfitter", "Safety Manager",
          "Sheet Metal Worker", "Steel fixer", "Steward", "Waterproofer", "Welder", "Other"]
TRADE_LVL = ["Not Applicable", "Apprentice", "Journeyperson", "Foreperson", "Supervisor"]
CSV_HEADER = 'Email* (required),First Name* (required),Last Name* (required),Year of Birth (YYYY),Address,City,' \
             'State/Province (2 letter code),Postal Code (A1A 1A1),Mobile Number (1-xxx-xxx-xxxx),Employee ID,' \
             'Trade,Trade Level\n'
PROVINCE = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]
POSTAL_CODES = ["G0S 2V0", "H2V 4J7", "T2T 3W6", "J2X 3S2", "K7P 2P9", "V2C 6A1", "V8P 1Z8", "G0A 3S0", "G0X 2Y0",
                "J5M 2S9", "G5Y 7W8", "J8P 8C3", "V3T 2T6", "S7M 0V9", "K1T 0C6", "J7G 3G3", "J0X 1H0", "L0M 1B2",
                "V3S 9K9", "N0B 2R0", "C0B 1B0", "A2H 3M2", "G4R 1H9", "J6A 2V3", "B0S 1B0", "G9H 1L2", "S7L 1X7",
                "E5J 2L2", "A2H 5W1", "M3K 1H5"]


def phone_gen():
    phone = "1-{}-{}-{}".format(random.randint(100, 999), random.randint(100, 999), random.randint(1000, 9999))
    # phone number should be like 1-xxx-xxx-xxxx
    return phone

def generate_data():
    result = '{},{},{},{},{},{},{},{},{},{},{},{}\n'\
        .format(fake.email(), fake.first_name(), fake.last_name(), random.randint(1920, 2010), fake.country(), fake.city(),
                random.choice(PROVINCE), random.choice(POSTAL_CODES), phone_gen(), random.randint(10000, 999999),
                random.choice(TRADES), random.choice(TRADE_LVL))
    return result

def set_rows_count(count):
    i = 0
    res = ''
    while i < count:
        res += generate_data()
        i += 1
    return res

def dump_to_csv(count):
    final_rows = '{}{}'.format(CSV_HEADER, set_rows_count(count))
    print(final_rows)
    with open('C:\\Users\\dkhad\\Desktop\\generated_data.csv', 'w') as f:
        f.write(final_rows)

if __name__ == "__main__":
    dump_to_csv(12)
