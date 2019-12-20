# -*- coding: utf-8 -*-
import unittest
import os

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from src.utils.db_postgress_helper import DbConnect
from src.pages.login_page import LoginPage
from src.pages.main_page import MainPage
from src.utils.api_helper import ApiHelper
from src.config_parser import Config
import time


class LoginTestSuite(unittest.TestCase):
    URL = 'https://acme.qc2.blnsearch.net/employer-client/certificates'

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(1700, 1000)
        self.driver.get(self.URL)
        self.email = Config.api_login
        self.password = Config.api_password

    def tearDown(self) -> None:
        self.driver.quit()

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.specify_email(self.email)
        login_page.specify_pass(self.password)
        login_page.press_login()

    def test_add_new_worker(self):
        fake = Faker()
        db_conn = DbConnect()
        email = fake.email()
        first_name = fake.first_name()
        last_name = fake.last_name()
        sql_query = """select "email" from "worker" where email='{}';""".format(email)
        login_page = LoginPage(self.driver)
        login_page.specify_email(self.email)
        login_page.specify_pass(self.password)
        login_page.press_login()
        main_page = MainPage(self.driver)
        main_page.press_add_new_worker()
        main_page.enter_email_address(email)
        main_page.press_search_emails()
        main_page.enter_first_name(first_name)
        main_page.enter_last_name(last_name)
        main_page.press_create_button()
        assert main_page.wait_for_confirm_message()
        query_response = db_conn.fetch_one(sql_query)
        self.assertIsNotNone(query_response)

    def test_edit_personal_data_via_profile(self):
        fake = Faker()
        db_conn = DbConnect()
        fake_email = fake.email()
        new_email = fake.email()
        new_first_name = fake.first_name()
        new_last_name = fake.last_name()
        body = {'email': fake_email, 'firstname': fake.first_name(), 'lastname': fake.last_name()}
        api_helper = ApiHelper()
        api_helper.do_post_request(os.path.join(Config.api_host, Config.api_get_workers_id_url), body)
        login_page = LoginPage(self.driver)
        login_page.specify_email(self.email)
        login_page.specify_pass(self.password)
        login_page.press_login()
        main_page = MainPage(self.driver)
        main_page.specify_search(fake_email)
        main_page.specify_search(Keys.ENTER)
        main_page.click_on_worker_name_in_grid()
        main_page.click_on_edit_profile()
        main_page.fill_fields_on_edit_pers_data(new_email, new_first_name, new_last_name)
        main_page.click_done_button()
        main_page.click_done_button()
        sql_query = """select "email" from "worker" where email='{}';""".format(new_email)
        query_response = db_conn.fetch_one(sql_query)
        self.assertIsNotNone(query_response)

    def test_archived_worker(self):
        fake = Faker()
        api_helper = ApiHelper()
        db_conn = DbConnect()
        email = fake.email()
        first_name = fake.first_name()
        last_name = fake.last_name()
        body = {'email': email, 'firstname': first_name, 'lastname': last_name}
        api_helper.do_post_request(os.path.join(Config.api_host, Config.api_get_workers_id_url), body)
        login_page = LoginPage(self.driver)
        login_page.specify_email(self.email)
        login_page.specify_pass(self.password)
        login_page.press_login()
        main_page = MainPage(self.driver)
        main_page.specify_search(email)
        main_page.specify_search(Keys.ENTER)
        main_page.click_on_checkbox_next_to_worker()
        main_page.click_on_archive_button()
        main_page.click_on_archive_button_in_dialog()
        sql_query = """select "email" from worker where email='{}' and archived='true';""".format(email)
        query_response = db_conn.fetch_one(sql_query)
        self.assertIsNotNone(query_response)

    def test_upload_file_via_profile(self):
        fake = Faker()
        api_helper = ApiHelper()
        db_conn = DbConnect()
        email = fake.email()
        first_name = fake.first_name()
        last_name = fake.last_name()
        cert_name = fake.company()
        body = {'email': email, 'firstname': first_name, 'lastname': last_name}
        api_helper.do_post_request(os.path.join(Config.api_host, Config.api_get_workers_id_url), body)
        login_page = LoginPage(self.driver)
        login_page.specify_email(self.email)
        login_page.specify_pass(self.password)
        login_page.press_login()
        main_page = MainPage(self.driver)
        main_page.specify_search(email)
        main_page.specify_search(Keys.ENTER)
        main_page.click_on_worker_name_in_grid()
        main_page.click_add_new_record()
        main_page.send_file_to_upload_input(os.path.join(os.path.abspath('..'), 'tmp', 'test.png'))
        main_page.select_from_drop_down()
        main_page.fill_data_for_certificate(cert_name, fake.company(), "2016-12-10", "2019-12-12", fake.company())
        sql_query = '''select "courseName" from "certificate" 
        where "workerId"=(select "id" from worker where email='{}') and "courseName"='{}';'''.format(email, cert_name)
        query_response = db_conn.fetch_one(sql_query)
        self.assertIsNotNone(query_response)
        time.sleep(5)
