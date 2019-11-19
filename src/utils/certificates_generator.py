import datetime
import os
import requests
import random

from faker import Faker

from src.config_parser import Config
from src.utils.api_helper import ApiHelper
from src.utils.db_postgress_helper import DbConnect


class CertificatesGenerator:
    def __init__(self):
        self.exp_date = "{}-11-05T16:01:38.440Z".format(random.randint(2017, 2030))
        self.image_file = "efb9c5a7-862b-46ca-9ce3-7c8110d0cbff_share rules.png"
        self.issued_date = "2017-11-05T16:01:38.433Z"
        self.url = os.path.join(Config.api_test_host, Config.api_test_post_path)
        self.fake = Faker('en_CA')
        api_helper = ApiHelper()
        self.token = api_helper.auth_token
        self.header = {'Authorization': 'bln type=session,version=1,token="{}"'.format(self.token)}

    @staticmethod
    def get_worker_id():
        db_conn = DbConnect()
        worker_id = db_conn.fetch_all('''select "id" from "worker" where "employerId"=201 and "archived"=false;''')
        return [x[0] for x in worker_id]

    def generate_payload(self, worker_id: int) -> dict:
        body = {'courseName': self.fake.company(),
                'description': self.fake.catch_phrase(),
                'expiration': self.exp_date,
                'file': self.image_file,
                'issued': self.issued_date,
                'trainingProvider': self.fake.company(),
                'workerId': worker_id
                }
        return body

    def add_certificates(self):
        for workers_id in self.get_worker_id():
            response = requests.post(self.url, headers=self.header, json=self.generate_payload(workers_id))
            if response.status_code == 201:
                print(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S -"), 'Certificate successfully created')
            else:
                print(response.status_code)


if __name__ == "__main__":
    c = CertificatesGenerator()
    c.add_certificates()
