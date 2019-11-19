import requests
from src.config_parser import Config


class ApiHelper:
    def __init__(self):
        self.auth_url = Config.api_test_host + Config.api_test_auth_path
        self.login = Config.api_test_login
        self.password = Config.api_test_password
        self.auth_token = self.auth_get_token()

    def auth_get_token(self):
        response = requests.post(self.auth_url,
                                 data={'grantType': "password_persistent",
                                       'identifier': "{}".format(self.login),
                                       'organizationKey': "acme",
                                       'password': "{}".format(self.password)})
        return response.json().get('token')

    def do_get_request(self, get_url):
        response = requests.get(get_url, headers={
            'Authorization': 'bln type=session,version=1,token="{}"'.format(self.auth_token)})
        return response

    def do_post_request(self, post_url, body):
        response = requests.post(post_url, headers={
            'Authorization': 'bln type=session,version=1,token="{}"'.format(self.auth_token())}, json=body)
        return response.status_code
