# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from src.pages.login_page import LoginPage
from src.pages.main_page import MainPage
import time


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

    # def test_login(self):
    #     login_page = LoginPage(self.driver)
    #     login_page.specify_email(self.email)
    #     login_page.specify_pass(self.password)
    #     login_page.press_login()

    def test_add_new_worker(self):
        email = "test@email.com"
        first_name = "Jack"
        last_name = "Daniels"
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



