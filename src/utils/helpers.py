import csv
import glob
import time
import os
import random

from faker import Faker

from src.utils.api_helper import Config
from src.utils.api_helper import ApiHelper
from src.utils.db_postgress_helper import DbConnect


class Helpers:
    def __init__(self):
        self.api_helper = ApiHelper()
        self.db_conn = DbConnect()
        self.fake = Faker()

    @staticmethod
    def get_count_of_emails_in_csv():
        def count_unique_emails():
            list_of_files = glob.glob('{}\\report*.csv'.format(Config.download_path))
            with open(list_of_files[0], 'r') as csv_report:
                csv_file = csv.DictReader(csv_report)
                emails_list = [dict(row).get('Email address') for row in csv_file]
                return len(set(emails_list))

        try:
            emails_number = count_unique_emails()
        except:
            time.sleep(1)
            emails_number = count_unique_emails()
        return emails_number

    def create_worker(self):
        fake_data = self.generate_fake_data()
        fake_email = fake_data["email"]
        body = {'email': fake_email,
                'firstname': fake_data["first_name"],
                'lastname': fake_data["last_name"]
                }
        response = self.api_helper.make_http_request(method_type="POST", url_part="workers_creation", body=body)
        return response.json().get('id')

    def create_multiple_workers(self, number):
        fake = Faker()
        names_list = []
        for i in range(number):
            body = {'email': fake.email(), 'firstname': fake.first_name(), 'lastname': fake.last_name()}
            self.api_helper.make_http_request(method_type="POST", url_part="workers_creation", body=body)
            names_list.append(body.get('firstname'))
            names_list.append(body.get('lastname'))
        return names_list

    @staticmethod
    def clear_download_folder():
        download_path = os.path.join(os.path.abspath('..'), 'tmp')
        list_csv_for_remove = glob.glob('{}\\*.csv'.format(download_path))
        [os.remove(csv_file) for csv_file in list_csv_for_remove]

    def set_no_primary_report(self):
        set_no_report_query = '''update "report" set "primary" = 'false' where "primary" = 'true';'''
        check_report_query = '''select "primary" from "report" where "primary" = 'true';'''
        query_response = self.db_conn.fetch_all(check_report_query)
        if query_response:
            self.db_conn.write_to_db(set_no_report_query)

    @staticmethod
    def gen_date():
        expiration_date = "{}-{}-{}T15:15:10.440Z".format(
            random.randint(2017, 2023),
            random.choice(["%.2d" % i for i in range(1, 12)]),
            random.choice(["%.2d" % i for i in range(1, 25)]))
        return expiration_date

    def generate_fake_data(self):
        fake_data = {
            "email": self.fake.email(),
            "email2": self.fake.email(),
            "first_and_last_name": self.fake.name(),
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
            "name_prefix": self.fake.prefix(),
            "cert_name": self.fake.company(),
            "cert_name2": self.fake.company(),
            "city": self.fake.city(),
            "country": self.fake.country(),
            "street_name": self.fake.street_name(),
            "random_phrase": self.fake.catch_phrase(),
            "random_phrase2": self.fake.catch_phrase(),
            "random_number": self.fake.ean(length=13)
        }
        return fake_data


