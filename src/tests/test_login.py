# -*- coding: utf-8 -*-
import unittest
import time

from selenium import webdriver

from src.pages.login_page import LoginPage
from src.pages.main_page import MainPage


class LoginTestSuite(unittest.TestCase):
    URL = 'https://acme.qc2.blnsearch.net'

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)
        self.email = 'admin@acme.com'
        self.password = 'password'
        self.stext = 'test'

    def tearDown(self) -> None:
        self.driver.quit()

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.specify_email(self.email)
        login_page.specify_pass(self.password)
        login_page.press_login()
        time.sleep(10)

    def test_main_page(self):
        main_page = MainPage(self.driver)
        main_page.specify_search(self.stext)
        time.sleep(10)



