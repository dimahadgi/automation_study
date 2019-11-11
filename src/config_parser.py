import configparser
import os


class Config:
    config = configparser.ConfigParser()
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '..', "db_conf.ini")
    config.read(file_path)
    user = config.get('db_connection_settings', 'user')
    password = config.get('db_connection_settings', 'password')
    host = config.get('db_connection_settings', 'host')
    port = config.get('db_connection_settings', 'port')
    database = config.get('db_connection_settings', 'database')


class ApiConf:
    config = configparser.ConfigParser()
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '..', "api_conf.ini")
    config.read(file_path)
    login = config.get('api_connection_settings', 'login')
    password = config.get('api_connection_settings', 'password')
    auth_url = config.get('api_connection_settings', 'auth_url')
