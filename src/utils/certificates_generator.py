import os
import requests
import random

from faker import Faker

from src.config_parser import Config
from src.utils.api_helper import ApiHelper
from src.utils.db_postgress_helper import DbConnect


def gen_date():
    expiration_date = "{}-{}-{}T15:15:10.440Z".format(
        random.randint(2017, 2023),
        random.choice(["%.2d" % i for i in range(1, 12)]),
        random.choice(["%.2d" % i for i in range(1, 25)]))
    return expiration_date


class CertificatesGenerator:
    def __init__(self):
        self.image_file = "efb9c5a7-862b-46ca-9ce3-7c8110d0cbff_share rules.png"
        self.issued_date = "2016-11-05T16:01:38.433Z"
        self.url = os.path.join(Config.api_host, Config.create_certs_path)
        self.fake = Faker('en_CA')
        self.api_helper = ApiHelper()
        self.token = self.api_helper.auth_token
        self.header = {'Authorization': 'bln type=session,version=1,token="{}"'.format(self.token)}

    def get_workers_id(self):
        if Config.env == "prod":
            workers_list = self.api_helper.do_get_request("workers_creation").json()
            return [d.get('id') for d in workers_list]
        else:
            db_conn = DbConnect()
            query = '''select "id" from "worker" where "employerId"={} and "archived"=false;'''.format(Config.db_login)
            worker_id = db_conn.fetch_all(query)
            return [x[0] for x in worker_id]

    def generate_payload(self, worker_id: int, course_names: str) -> dict:
        body = {'courseName': course_names,
                'description': self.fake.catch_phrase(),
                'expiration': gen_date(),
                'file': self.image_file,
                'issued': self.issued_date,
                'trainingProvider': self.fake.company(),
                'workerId': worker_id
                }
        return body

    def add_certificates(self, course_names: list):
        certificates_id = []
        for worker_id in self.get_workers_id():
            response = requests.post(self.url,
                                     headers=self.header,
                                     json=self.generate_payload(worker_id, random.choice(course_names)))
            certificates_id.append(response.json().get('id'))
            if response.status_code == 201:
                pass
            else:
                print("Certificate is not created", response.status_code)
                break
        return certificates_id


if __name__ == "__main__":
    fake = Faker('en_CA')
    cert_gen = CertificatesGenerator()
    cert_gen.add_certificates([fake.company() for x in range(0, 5)])


