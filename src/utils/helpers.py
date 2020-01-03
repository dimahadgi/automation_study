import csv
import glob
import os
import time

DOWNLOAD_PATH = os.path.join(os.path.abspath('..'), 'tmp')


def parse_csv_file():
    def count_emails():
        list_of_files = glob.glob(DOWNLOAD_PATH + '\\report*.csv')
        with open(list_of_files[0], 'r') as file:
            csv_file = csv.DictReader(file)
            emails_list = [dict(row).get('Email address') for row in csv_file]
            return len(set(emails_list))
    try:
        emails_number = count_emails()
    except:
        time.sleep(1)
        emails_number = count_emails()
    return emails_number


