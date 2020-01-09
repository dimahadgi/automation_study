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
from src.utils.helpers import Helpers


class LoginTestSuite(unittest.TestCase):
    def setUp(self):
        self.url = Config.login_url
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("prefs", {
            "download.default_directory": Config.download_path,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.driver.get(self.url)
        self.helpers = Helpers()
        self.helpers.set_no_primary_report()

    def tearDown(self) -> None:
        self.driver.quit()
        helpers = Helpers()
        helpers.clear_download_folder()

    def login(self, email=Config.api_first_login, password=Config.api_password):
        login_page = LoginPage(self.driver)
        login_page.specify_email(email)
        login_page.specify_pass(password)
        login_page.press_login()

    def test_login(self):
        main_page = MainPage(self.driver)
        self.login()
        self.assertTrue(main_page.wait_for_grid_render())

    def test_add_new_worker(self):
        main_page = MainPage(self.driver)
        db_conn = DbConnect()
        fake_data = generate_fake_data()
        email = fake_data["email"]
        sql_query = """select "email" from "worker" where email='{}';""".format(email)
        self.login()
        main_page.press_add_new_worker()
        main_page.enter_email_address(email)
        main_page.press_search_emails()
        main_page.enter_first_name(fake_data["first_name"])
        main_page.enter_last_name(fake_data["last_name"])
        main_page.press_create_button()
        self.assertTrue(main_page.wait_for_confirm_message())
        query_response = db_conn.fetch_one(sql_query)
        self.assertIsNotNone(query_response)

    def test_edit_personal_data_via_profile(self):
        db_conn = DbConnect()
        api_helper = ApiHelper()
        main_page = MainPage(self.driver)
        fake_data = generate_fake_data()
        fake_data2 = generate_fake_data()
        fake_email = fake_data["email"]
        new_email = fake_data2["email"]
        sql_query = """select "email" from "worker" where email='{}';""".format(new_email)
        body = {'email': fake_email,
                'firstname': fake_data["first_name"],
                'lastname': fake_data["last_name"]
                }
        api_helper.make_http_request(method_type="POST", url_part="workers_creation", body=body)
        self.login()
        main_page.specify_search(fake_email)
        main_page.press_search_button()
        main_page.click_on_worker_name_in_grid()
        main_page.click_on_edit_profile()
        main_page.fill_fields_on_edit_pers_data(new_email,
                                                fake_data2["first_name"],
                                                fake_data2["last_name"])
        main_page.click_done_button()
        main_page.click_done_button()
        query_response = db_conn.fetch_one(sql_query)
        self.assertIsNotNone(query_response)

    def test_archived_worker(self):
        main_page = MainPage(self.driver)
        api_helper = ApiHelper()
        db_conn = DbConnect()
        fake_data = generate_fake_data()
        email = fake_data["email"]
        sql_query = """select "email" from worker where email='{}' and archived='true';""".format(email)
        body = {'email': email,
                'firstname': fake_data["first_name"],
                'lastname': fake_data["last_name"]
                }
        api_helper.make_http_request(method_type="POST", url_part="workers_creation", body=body)
        self.login()
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
        fake_data = generate_fake_data()
        fake_data2 = generate_fake_data()
        image_path = os.path.join(os.path.abspath('..'), 'tmp', 'test.png')
        email = fake_data["email"]
        cert_name = fake_data["cert_name"]
        body = {'email': email,
                'firstname': fake_data["first_name"],
                'lastname': fake_data["last_name"]
                }
        sql_query = '''select "courseName" from "certificate" 
                where "workerId"=(select "id" from worker where email='{}') 
                and "courseName"='{}';'''.format(email, cert_name)
        api_helper.make_http_request(method_type="POST", url_part="workers_creation", body=body)
        self.login()
        main_page.specify_search(email)
        main_page.press_search_button()
        main_page.click_on_worker_name_in_grid()
        main_page.click_add_new_record()
        main_page.send_file_to_upload_input(image_path)
        main_page.select_from_drop_down()
        main_page.type_certificate_name(cert_name)
        main_page.type_tr_provider_name(fake_data2["cert_name"])
        main_page.type_dates("2016-12-10", "2019-12-12")
        main_page.type_additional_info(fake_data2["cert_name"])
        main_page.press_submit_button()
        query_response = db_conn.fetch_one(sql_query)
        self.assertIsNotNone(query_response)

    def test_edit_certificates(self):
        main_page = MainPage(self.driver)
        api_helper = ApiHelper()
        db_conn = DbConnect()
        fake_data = generate_fake_data()
        fake_data2 = generate_fake_data()
        email = fake_data["email"]
        first_name = fake_data["first_name"]
        last_name = fake_data["last_name"]
        image_file = "efb9c5a7-862b-46ca-9ce3-7c8110d0cbff_share rules.png"
        query = """select "id" from worker where email='{}';""".format(email)
        worker_body = {'email': email, 'firstname': first_name, 'lastname': last_name}
        api_helper.make_http_request(method_type="POST", url_part="workers_creation", body=worker_body)
        worker_id = db_conn.fetch_one(query)[0]
        cert_body = {'courseName': fake_data["cert_name"],
                     'description': fake_data["random_phrase"],
                     'expiration': "2030-11-05T16:01:38.433Z",
                     'file': image_file,
                     'issued': "2016-11-05T16:01:38.433Z",
                     'trainingProvider': fake_data2["cert_name"],
                     'workerId': worker_id
                     }
        certificate_query = """select "courseName" from "certificate" where "workerId"=(
        select "id" from worker where email='{}') 
        and "courseName"='{}' 
        and "description"='{}' 
        and "trainingProvider"='{}' 
        and "file"='{}';""".format(email, "Certificate name after EDITING",
                                   "Additional Certificate Details after EDITING",
                                   "Training Provider Name after EDITING", image_file)
        api_helper.make_http_request(method_type="POST", url_part="certificates_creation", body=cert_body)
        self.login()
        main_page.specify_search(email)
        main_page.press_search_button()
        main_page.click_on_worker_name_in_grid()
        main_page.click_edit_certificates_control()
        main_page.type_certificate_name("Certificate name after EDITING")
        main_page.type_tr_provider_name("Training Provider Name after EDITING")
        main_page.type_dates("2000-01-01", "2040-12-12")
        main_page.type_additional_info("Additional Certificate Details after EDITING")
        main_page.press_submit_button()
        query_response = db_conn.fetch_one(certificate_query)
        self.assertIsNotNone(query_response)

    def test_save_teams(self):
        db_conn = DbConnect()
        main_page = MainPage(self.driver)
        fake_data = generate_fake_data()
        team_name = fake_data["cert_name"]
        sql_query = '''select "name" from "team" where name='{}';'''.format(team_name)
        self.login()
        main_page.click_on_checkbox_next_to_worker(1)
        main_page.click_on_checkbox_next_to_worker(2)
        main_page.click_on_checkbox_next_to_worker(3)
        main_page.click_on_checkbox_next_to_worker(4)
        main_page.click_on_checkbox_next_to_worker(5)
        main_page.click_save_team_button()
        main_page.type_team_name_while_saving(team_name)
        main_page.click_save_button_while_saving_team()
        main_page.click_done_button()
        query_response = db_conn.fetch_one(sql_query)
        self.assertIsNotNone(query_response)

    def test_verify_project_team_filter(self):
        main_page = MainPage(self.driver)
        api_helper = ApiHelper()
        fake_data = generate_fake_data()
        team_name = fake_data["cert_name"]
        worker_id = self.helpers.create_worker()
        body = {'name': team_name, 'workerIds': [worker_id]}
        api_helper.make_http_request(method_type="POST", url_part="teams_creation", body=body)
        self.login()
        main_page.open_project_teams_filter()
        main_page.mark_checkbox_in_modals()
        main_page.click_apply_button_in_modals()
        self.assertTrue(main_page.verify_chips_is_present())
        main_page.select_all_workers_in_the_grid()
        self.assertTrue(main_page.verify_text_of_counting_worker())

    def test_share_workers_to_another_employee(self):
        main_page = MainPage(self.driver)
        fake_data = generate_fake_data()
        recipient_name = fake_data["cert_name"]
        recipient_email = Config.api_second_login
        recipient_company_name = fake_data["random_phrase2"]
        project_name = fake_data["cert_name2"]
        comments = fake_data["random_phrase"]
        names_list = self.helpers.create_multiple_workers(5)
        self.login()
        main_page.click_on_checkbox_next_to_worker(1)
        main_page.click_on_checkbox_next_to_worker(2)
        main_page.click_on_checkbox_next_to_worker(3)
        main_page.click_on_checkbox_next_to_worker(4)
        main_page.click_on_checkbox_next_to_worker(5)
        main_page.click_share_team_button()
        main_page.fill_recipient_name_while_sharing(recipient_name)
        main_page.fill_recipient_email_while_sharing(recipient_email)
        main_page.fill_recipient_company_name_while_sharing(recipient_company_name)
        main_page.fill_project_name_while_sharing(project_name)
        main_page.fill_comments_for_recipient_while_sharing(comments)
        main_page.click_share_button()
        main_page.click_done_button()
        main_page.click_sign_out()
        self.login(Config.api_second_login)
        self.assertTrue(main_page.wait_for_grid_render())
        main_page.click_shared_button()
        main_page.mark_checkboxes_in_shared_modal()
        main_page.click_apply_button_in_modals()
        main_page.wait_for_grid_render()
        self.assertTrue(main_page.check_name_exist_in_grid(names_list[0]))
        self.assertTrue(main_page.check_name_exist_in_grid(names_list[1]))
        self.assertTrue(main_page.check_name_exist_in_grid(names_list[2]))
        self.assertTrue(main_page.check_name_exist_in_grid(names_list[3]))
        self.assertTrue(main_page.check_name_exist_in_grid(names_list[4]))

    def test_sync_button(self):
        main_page = MainPage(self.driver)
        self.login()
        main_page.click_sync_button()
        main_page.wait_for_sync()
        self.assertTrue(main_page.wait_for_grid_render())

    def test_download_csv(self):
        main_page = MainPage(self.driver)
        db_conn = DbConnect()
        self.login()
        main_page.click_download_csv_button()
        sql_query = '''select count(email) 
        from worker where "employerId"='{}' and archived='False';'''.format(Config.db_login)
        query_response = db_conn.fetch_one(sql_query)
        self.assertEqual(self.helpers.get_count_of_emails_in_csv(), query_response[0])

    def test_validate_main_search(self):
        main_page = MainPage(self.driver)
        api_helper = ApiHelper()
        fake_data = generate_fake_data()
        email = fake_data["email"]
        f_name = "{} {}".format(fake_data["name_prefix"], fake_data["first_name"])
        l_name = fake_data["last_name"]
        first_and_last_name = "{} {}".format(f_name, l_name)
        employee_id = fake_data["random_number"]
        body = {'email': email, 'firstname': f_name, 'lastname': l_name, 'employeeId': employee_id}
        api_helper.make_http_request(method_type="POST", url_part="workers_creation", body=body)
        self.login()
        # search by first and last name
        main_page.specify_search(first_and_last_name)
        main_page.press_search_button()
        self.assertTrue(main_page.check_name_exist_in_grid(first_and_last_name))
        # search by email
        main_page.clear_search_filed()
        main_page.specify_search(email)
        main_page.press_search_button()
        self.assertTrue(main_page.check_name_exist_in_grid(first_and_last_name))
        # search by worker's employee id
        main_page.clear_search_filed()
        main_page.specify_search(employee_id)
        main_page.press_search_button()
        self.assertTrue(main_page.check_name_exist_in_grid(first_and_last_name))





