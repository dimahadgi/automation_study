import csv
import glob
import time
import os

from src.utils.api_helper import Config
from src.utils.api_helper import ApiHelper
from src.utils.data_generator import generate_fake_data


def parse_csv_file():
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


def create_worker():
    fake_data = generate_fake_data()
    fake_email = fake_data["email"]
    api_helper = ApiHelper()
    body = {'email': fake_email,
            'firstname': fake_data["first_name"],
            'lastname': fake_data["last_name"]
            }
    response = api_helper.make_http_request(method_type="POST", url_part="workers_creation", body=body)
    return response.json().get('id')


def clear_download_folder():
    download_path = os.path.join(os.path.abspath('..'), 'tmp')
    list_csv_for_remove = glob.glob('{}\\*.csv'.format(download_path))
    [os.remove(csv_file) for csv_file in list_csv_for_remove]
