import requests
import os

from src.config_parser import Config


class ApiHelper:
    def __init__(self):
        self.auth_url = os.path.join(Config.api_host, Config.api_auth_path)
        self.organization_key = Config.api_organization_key
        self.login = Config.api_login
        self.password = Config.api_password
        self.auth_token = self.auth_get_token()
        self.header = {'Authorization': 'bln type=session,version=1,token="{}"'.format(self.auth_token)}
        self.post_url = os.path.join(Config.api_host, Config.api_get_workers_id_url)

    def auth_get_token(self):
        response = requests.post(self.auth_url,
                                 data={'grantType': "password_persistent",
                                       'identifier': self.login,
                                       'organizationKey': self.organization_key,
                                       'password': self.password})
        return response.json().get('token')

    def do_get_request(self, get_url):
        response = requests.get(get_url, headers=self.header)
        return response

    def do_post_request(self, body):
        response = requests.post(self.post_url, headers=self.header, json=body)
        return response


if __name__ == "__main__":
    api = ApiHelper()
    api.auth_get_token()
