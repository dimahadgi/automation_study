import configparser
import os


class Config:
    config = configparser.ConfigParser()
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '..', "conf.ini")
    config.read(file_path)
    db_user = config.get('db_connection_settings', 'user')
    db_password = config.get('db_connection_settings', 'password')
    db_host = config.get('db_connection_settings', 'host')
    db_port = config.get('db_connection_settings', 'port')
    db_database = config.get('db_connection_settings', 'database')

    api_test_login = config.get('test', 'login1')
    api_test_password = config.get('test', 'password')
    api_test_host = config.get('test', 'host')
    api_test_auth_path = config.get('test', 'auth_path')
    api_test_post_path = config.get('test', 'post_path')
    api_test_get_workers_id_url = config.get('test', 'get_workers_id_url')
