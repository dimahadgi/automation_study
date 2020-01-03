import requests
import os

from src.config_parser import Config
from requests.exceptions import HTTPError


class ApiHelper:
    API_ROUTES = {
        'certificates_creation': Config.create_certs_path,
        'workers_creation': Config.api_get_workers_id_url,
        'teams_creation': Config.create_teams
    }

    def __init__(self):
        self.auth_url = os.path.join(Config.api_host, Config.api_auth_path)
        self.organization_key = Config.api_organization_key
        self.login = Config.api_first_login
        self.password = Config.api_password
        self.auth_token = self.auth_get_token()
        self.header = {'Authorization': 'bln type=session,version=1,token="{}"'.format(self.auth_token)}
        self.url = Config.api_host

    def auth_get_token(self):
        response = requests.post(self.auth_url,
                                 data={'grantType': "password_persistent",
                                       'identifier': self.login,
                                       'organizationKey': self.organization_key,
                                       'password': self.password})
        return response.json().get('token')

    def do_get_request(self, url_part):
        try:
            response = requests.get(os.path.join(self.url, self.API_ROUTES[url_part]), headers=self.header)
            response.raise_for_status()
            return response
        except HTTPError:
            raise
        except Exception:
            raise

    def do_post_request(self, url_part, body):
        try:
            response = requests.post(os.path.join(self.url, self.API_ROUTES[url_part]), headers=self.header, json=body)
            response.raise_for_status()
            return response
        except HTTPError:
            raise
        except Exception:
            raise


if __name__ == "__main__":
    api = ApiHelper()
    api.auth_get_token()
