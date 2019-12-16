# -*- coding: utf-8 -*-
import unittest

from faker import Faker
from selenium import webdriver

from src.utils.db_postgress_helper import DbConnect
from src.pages.login_page import LoginPage
from src.pages.main_page import MainPage


class LoginTestSuite(unittest.TestCase):
    URL = 'https://acme.qc2.blnsearch.net/employer-client/certificates'

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(1700, 1000)
        self.driver.get(self.URL)
        self.email = 'admin@acme.com'
        self.password = 'password'

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
        main_page.wait_for_confirm_message()
        query_response = db_conn.fetch_one(sql_query)
        self.assertIsNotNone(query_response)
