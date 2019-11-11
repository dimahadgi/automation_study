import requests
import random

from src.utils.db_postgress_helper import DbConnect
from faker import Faker
fake = Faker('en_CA')

POST_URL = "https://acme.qc2.blnsearch.net/api-employer/certificates"
GET_URL = "https://acme.qc2.blnsearch.net/api-employer/workers?sort=created&order=desc&$limit=1000"


def get_worker_id():
    dbconn = DbConnect()
    worker_id = dbconn.fetch_all('''select "id" from "worker" where "employerId"=201 and "archived"=false;''')
    return [x[0] for x in worker_id]


def auth_get_token():
    response = requests.post('https://acme.qc2.blnsearch.net/auth/sessions',
                             data={'grantType': "password_persistent",
                                   'identifier': "admin@acme.com",
                                   'organizationKey': "acme",
                                   'password': "password"})
    token = response.json().get('token')
    return token


def do_get_request():
    response = requests.get(GET_URL, headers={'Authorization': 'bln type=session,version=1,token="{}"'.format(auth_get_token())})
    return response


def generate_payload(workers_id):
    body = {'courseName': "{}".format(fake.company()),
            'description': "{}".format(fake.catch_phrase()),
            'expiration': "{}-11-05T16:01:38.440Z".format(random.randint(2017, 2030)),
            'file': "efb9c5a7-862b-46ca-9ce3-7c8110d0cbff_share rules.png",
            'issued': "2017-11-05T16:01:38.433Z",
            'trainingProvider': "{}".format(fake.company()),
            'workerId': workers_id}
    return body


def do_post_request():
    for workers_id in get_worker_id():
        response = requests.post(POST_URL,
                                 headers={
                                     'Authorization': 'bln type=session,version=1,token="{}"'.format(auth_get_token())},
                                 json=generate_payload(workers_id))
        if response.status_code == 201:
            print('Certificate successfully added')
        else:
            print(response.status_code, generate_payload(workers_id))
    return response.content

do_post_request()

