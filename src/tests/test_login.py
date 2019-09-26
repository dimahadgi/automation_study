# -*- coding: utf-8 -*-
import unittest
import time

from selenium import webdriver

from src.pages.login_page import LoginPage


class LoginTestSuite(unittest.TestCase):

    URL = 'https://acme.qc2.blnsearch.net'

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/home/okura/PycharmProjects/chromedriver')
        self.driver.get(self.URL)
        self.email = 'admin@acme.com'
        self.password = 'password'

    def tearDown(self) -> None:
        self.driver.quit()

    def test_login(self):
        time.sleep(10)
        login_page = LoginPage(self.driver)
        time.sleep(5)
        login_page.specify_email(self.email)
        time.sleep(5)
        login_page.specify_pass(self.password)
        time.sleep(10)
        login_page.press_login()
