import random
import names
import string
from faker import Faker

fake = Faker('en_CA')
domains = ["hotmail.com", "gmail.com", "mail.com" , "mail.ru", "yahoo.com"]
trades = ["Boilermaker", "Carpenter", "Cement & Concrete Finisher" , "Construction Office Manager", "Crane Operator"]
letters = string.ascii_letters

def yob_gen(a, b):
    for x in range(1):
        v = random.randint(a, b)
        return v

def name_gen():
    z = names.get_first_name() + "," + names.get_last_name()
    return z

def create_csv():
    f = open('C:\\Users\\dkhad\\Desktop\\generated_data.csv', 'w')
    f.write(fin_res)
    f.close

def email_gen():
    i = 0
    mail = ''
    while i < 15:
        mail = mail + random.choice(letters)
        i += 1
    return mail + '@' + random.choice(domains)

i = 0
fin_res = 'Email* (required),First Name* (required),Last Name* (required),Year of Birth (YYYY),Address,City,State/Province (2 letter code),' \
          'Postal Code (A1A 1A1),Mobile Number (1-xxx-xxx-xxxx),Employee ID,Trade,Trade Level \n'
while i < 3:
    #result = email_gen() + ',' + name_gen() + ',' + str(yob_gen()) + ',' + random.choice(trades) + '\n'
    result = fake.email() + ',' + name_gen() + ',' + str(yob_gen(1919, 2019)) + ',' + fake.country() +  ',' \
             + fake.city() + ',' + fake.province_abbr() + ',' + fake.postalcode() + ', ,' + 'ID' + \
             str(yob_gen(100000, 999999)) + ',' + random.choice(trades) + ', ,' + '\n'
    fin_res = fin_res + result
    i += 1

create_csv()



#print(fin_res)