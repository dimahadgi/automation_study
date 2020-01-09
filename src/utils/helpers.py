import csv
import glob
import time
import os

from faker import Faker

from src.utils.api_helper import Config
from src.utils.api_helper import ApiHelper
from src.utils.data_generator import generate_fake_data
from src.utils.db_postgress_helper import DbConnect


class Helpers:
    def get_count_of_emails_in_csv(self):
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
        fake_data = generate_fake_data()
        fake_email = fake_data["email"]
        api_helper = ApiHelper()
        body = {'email': fake_email,
                'firstname': fake_data["first_name"],
                'lastname': fake_data["last_name"]
                }
        response = api_helper.make_http_request(method_type="POST", url_part="workers_creation", body=body)
        return response.json().get('id')

    def create_multiple_workers(self, number):
        api_helper = ApiHelper()
        fake = Faker()
        names_list = []
        for i in range(number):
            body = {'email': fake.email(), 'firstname': fake.first_name(), 'lastname': fake.last_name()}
            api_helper.make_http_request(method_type="POST", url_part="workers_creation", body=body)
            names_list.append(body.get('firstname'))
            names_list.append(body.get('lastname'))
        return names_list

    def clear_download_folder(self):
        download_path = os.path.join(os.path.abspath('..'), 'tmp')
        list_csv_for_remove = glob.glob('{}\\*.csv'.format(download_path))
        [os.remove(csv_file) for csv_file in list_csv_for_remove]

    def set_no_primary_report(self):
        db_conn = DbConnect()
        set_no_report_query = '''update "report" set "primary" = 'false' where "primary" = 'true';'''
        check_report_query = '''select "primary" from "report" where "primary" = 'true';'''
        query_response = db_conn.fetch_all(check_report_query)
        if query_response:
            db_conn.write_to_db(set_no_report_query)

if __name__ == "__main__":
    helpers = Helpers()
    helpers.set_no_primary_report()

