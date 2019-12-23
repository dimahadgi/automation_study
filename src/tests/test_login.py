# -*- coding: utf-8 -*-
import unittest
import os

from selenium import webdriver

from src.utils.db_postgress_helper import DbConnect
from src.pages.login_page import LoginPage
from src.pages.main_page import MainPage
from src.utils.api_helper import ApiHelper
from src.config_parser import Config
from src.utils.data_generator import generate_fake_data


class LoginTestSuite(unittest.TestCase):
    def setUp(self):
        self.url = Config.login_url
        self.driver = webdriver.Chrome()
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(1700, 1000)
        self.driver.get(self.url)
        self.email = Config.api_login
        self.password = Config.api_password

    def tearDown(self) -> None:
        self.driver.quit()

    def login(self):
        login_page = LoginPage(self.driver)
        login_page.specify_email(self.email)
        login_page.specify_pass(self.password)
        login_page.press_login()

    def test_login(self):
        main_page = MainPage(self.driver)
        self.login()
        self.assertTrue(main_page.wait_main_page())

    def test_add_new_worker(self):
        main_page = MainPage(self.driver)
        db_conn = DbConnect()
        email = generate_fake_data()["email"]
        sql_query = """select "email" from "worker" where email='{}';""".format(email)
        LoginTestSuite.login(self)
        main_page.press_add_new_worker()
        main_page.enter_email_address(email)
        main_page.press_search_emails()
        main_page.enter_first_name(generate_fake_data()["first_name"])
        main_page.enter_last_name(generate_fake_data()["last_name"])
        main_page.press_create_button()
        self.assertTrue(main_page.wait_for_confirm_message())
        query_response = db_conn.fetch_one(sql_query)
        self.assertIsNotNone(query_response)

    def test_edit_personal_data_via_profile(self):
        db_conn = DbConnect()
        api_helper = ApiHelper()
        main_page = MainPage(self.driver)
        fake_email = generate_fake_data()["email"]
        new_email = generate_fake_data()["email"]
        sql_query = """select "email" from "worker" where email='{}';""".format(new_email)
        body = {'email': fake_email,
                'firstname': generate_fake_data()["first_name"],
                'lastname': generate_fake_data()["last_name"]
                }
        api_helper.do_post_request(body)
        LoginTestSuite.login(self)
        main_page.specify_search(fake_email)
        main_page.press_search_button()
        main_page.click_on_worker_name_in_grid()
        main_page.click_on_edit_profile()
        main_page.fill_fields_on_edit_pers_data(new_email,
                                                generate_fake_data()["first_name"],
                                                generate_fake_data()["last_name"])
        main_page.click_done_button()
        main_page.click_done_button()
        query_response = db_conn.fetch_one(sql_query)
        self.assertIsNotNone(query_response)

    def test_archived_worker(self):
        main_page = MainPage(self.driver)
        api_helper = ApiHelper()
        db_conn = DbConnect()
        email = generate_fake_data()["email"]
        sql_query = """select "email" from worker where email='{}' and archived='true';""".format(email)
        body = {'email': email,
                'firstname': generate_fake_data()["first_name"],
                'lastname': generate_fake_data()["last_name"]
                }
        api_helper.do_post_request(body)
        LoginTestSuite.login(self)
        main_page.specify_search(email)
        main_page.press_search_button()
        main_page.click_on_checkbox_next_to_worker()
        main_page.click_on_archive_button()
        main_page.click_on_archive_button_in_dialog()
        query_response = db_conn.fetch_one(sql_query)
        self.assertIsNotNone(query_response)

    def test_upload_file_via_profile(self):
        main_page = MainPage(self.driver)
        api_helper = ApiHelper()
        db_conn = DbConnect()
        image_path = os.path.join(os.path.abspath('..'), 'tmp', 'test.png')
        email = generate_fake_data()["email"]
        cert_name = generate_fake_data()["cert_name"]
        body = {'email': email,
                'firstname': generate_fake_data()["first_name"],
                'lastname': generate_fake_data()["last_name"]
                }
        sql_query = '''select "courseName" from "certificate" 
                where "workerId"=(select "id" from worker where email='{}') 
                and "courseName"='{}';'''.format(email, cert_name)
        api_helper.do_post_request(body)
        LoginTestSuite.login(self)
        main_page.specify_search(email)
        main_page.press_search_button()
        main_page.click_on_worker_name_in_grid()
        main_page.click_add_new_record()
        main_page.send_file_to_upload_input(image_path)
        main_page.select_from_drop_down()
        main_page.fill_data_for_certificate(cert_name,
                                            generate_fake_data()["cert_name"],
                                            "2016-12-10",
                                            "2019-12-12",
                                            generate_fake_data()["cert_name"])
        query_response = db_conn.fetch_one(sql_query)
        self.assertIsNotNone(query_response)
