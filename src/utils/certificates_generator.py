import os
import requests
import random

from faker import Faker

from src.config_parser import Config
from src.utils.api_helper import ApiHelper
from src.utils.db_postgress_helper import DbConnect


class CertificatesGenerator:
    def __init__(self):
        self.exp_date = "{}-11-05T16:01:38.440Z".format(random.randint(2017, 2023))
        self.image_file = "efb9c5a7-862b-46ca-9ce3-7c8110d0cbff_share rules.png"
        self.issued_date = "2017-11-05T16:01:38.433Z"
        self.url = os.path.join(Config.api_host, Config.create_certs_path)
        self.get_id_url = os.path.join(Config.api_host, Config.api_get_workers_id_url)
        self.fake = Faker('en_CA')
        self.api_helper = ApiHelper()
        self.token = self.api_helper.auth_token
        self.header = {'Authorization': 'bln type=session,version=1,token="{}"'.format(self.token)}

    @staticmethod
    def get_worker_id_from_db():
        db_conn = DbConnect()
        worker_id = db_conn.fetch_all('''select "id" from "worker" where "employerId"=201 and "archived"=false;''')
        return [x[0] for x in worker_id]

    def get_workers_id_from_api(self):
        workers_list = self.api_helper.do_get_request(self.get_id_url).json()
        return [d.get('id') for d in workers_list]

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
        certificates_id = []
        for workers_id in self.get_workers_id_from_api():
            response = requests.post(self.url, headers=self.header, json=self.generate_payload(workers_id))
            certificates_id.append(response.json().get('id'))
            if response.status_code == 201:
                pass
            else:
                print("Certificate is not created", response.status_code)
                break
        return certificates_id


if __name__ == "__main__":
    cert_gen = CertificatesGenerator()
    cert_gen.add_certificates()
