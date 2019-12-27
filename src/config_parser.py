import configparser
import os


class Config:
    config = configparser.ConfigParser()
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '..', "conf.ini")
    config.read(file_path)

    # login_url
    login_url = config.get('login_params', 'url')

    # Environment
    env = config.get('api_params', 'env')

    # Database parameters
    db_user = config.get('db_params', 'user')
    db_password = config.get('db_params', 'password')
    db_host = config.get('db_params', 'host')
    db_port = config.get('db_params', 'port')
    db_database = config.get('db_params', 'database')
    db_login = config.get('db_params', 'login')

    # API parameters
    api_login = config.get('api_params', 'login')
    api_password = config.get('api_params', 'password')
    api_host = config.get('api_params', 'host')
    api_auth_path = config.get('api_params', 'auth_path')
    create_teams = config.get('api_params', 'create_teams')
    create_certs_path = config.get('api_params', 'create_certs_path')
    api_get_workers_id_url = config.get('api_params', 'get_workers_id_url')
    api_organization_key = config.get('api_params', 'organization_key')
