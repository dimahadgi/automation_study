import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from src.pages.base_page import BasePage
from src.locators import main_page_locators as locators


class MainPage(BasePage):
    def wait_main_page(self):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locators.CERTIFICATES_TAB))
            return True
        except NoSuchElementException:
            return False

    def press_add_new_worker(self):
        add_new_worker = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.ADD_NEW_WORKER))
        add_new_worker.click()

    def enter_email_address(self, email):
        enter_email = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.EMAIL_ADDRESS_FIELD))
        enter_email.send_keys(email)

    def press_search_emails(self):
        press_search = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.SEARCH_EMAILS_BUTTON))
        press_search.click()

    def enter_first_name(self, name):
        enter_first_name = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.FIRST_NAME_FIELD))
        enter_first_name.send_keys(name)

    def enter_last_name(self, name):
        enter_last_name = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.LAST_NAME_FIELD))
        enter_last_name.send_keys(name)

    def press_create_button(self):
        press_create = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.CREATE_WORKER_BUTTON))
        press_create.click()

    def wait_for_confirm_message(self):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locators.CONFIRMATION_MESSAGE))
            return True
        except NoSuchElementException:
            return False

    def click_on_worker_name_in_grid(self, index=0):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locators.WORKER_IN_THE_GRID))
        worker_in_grid = self.driver.find_elements(*locators.WORKER_IN_THE_GRID)
        worker_in_grid[index].click()

    def click_on_edit_profile(self):
        edit_profile_control = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.EDIT_PROFILE_CONTROL))
        edit_profile_control.click()

    def specify_search(self, text):
        def wait_for_search():
            search_field = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locators.SEARCH))
            search_field.send_keys(text)
        try:
            wait_for_search()
        except:
            time.sleep(1)
            wait_for_search()

    def press_search_button(self):
        submit_button = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.SUBMIT_BUTTON))
        submit_button.click()

    def fill_fields_on_edit_pers_data(self, new_email, new_first_name, new_last_name):
        first_name = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.FIRST_NAME_FIELD))
        last_name = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.LAST_NAME_FIELD))
        email_field = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.EMAIL_FIELD_IN_EDIT_MODAL))
        first_name.send_keys(Keys.CONTROL + "a")
        first_name.send_keys(Keys.DELETE)
        first_name.send_keys(new_first_name)
        last_name.send_keys(Keys.CONTROL + "a")
        last_name.send_keys(Keys.DELETE)
        last_name.send_keys(new_last_name)
        email_field.send_keys(Keys.CONTROL + "a")
        email_field.send_keys(Keys.DELETE)
        email_field.send_keys(new_email)

    def click_done_button(self):
        done_button = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.DONE_BUTTON_IN_EDIT_MODAL))
        done_button.click()

    def click_add_new_record(self):
        add_new_record = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.ADD_NEW_RECORD))
        add_new_record.click()

    def send_file_to_upload_input(self, path):
        element = self.driver.find_element(*locators.INPUT_FOR_UPLOAD_BUTTON)
        element.send_keys(path)

    def select_from_drop_down(self):
        drop_down = self.driver.find_element(*locators.SELECT_DROP_DOWN)
        drop_down.click()
        first_item = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.FIRST_ITEM_IN_DROP_DOWN))
        first_item.click()

    def type_certificate_name(self, cert_name):
        certificate_title = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.CERTIFICATE_TITLE))
        certificate_title.send_keys(cert_name + Keys.ENTER)

    def type_tr_provider_name(self, tr_name):
        training_provider = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.TRAINING_PROVIDER_NAME))
        training_provider.send_keys(Keys.CONTROL + "a")
        training_provider.send_keys(Keys.DELETE)
        training_provider.send_keys(tr_name)

    def type_dates(self, iss_date, exp_date):
        issued_date = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.ISSUED_DATE))
        issued_date.send_keys(Keys.CONTROL + "a")
        issued_date.send_keys(Keys.DELETE)
        issued_date.send_keys(iss_date)
        expiry_date = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.EXPIRY_DATE))
        expiry_date.send_keys(Keys.CONTROL + "a")
        expiry_date.send_keys(Keys.DELETE)
        expiry_date.send_keys(exp_date)

    def type_additional_info(self, add_detail):
        add_field = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.ADDITIONAL_DETAILS_FIELD))
        add_field.send_keys(Keys.CONTROL + "a")
        add_field.send_keys(Keys.DELETE)
        add_field.send_keys(add_detail)

    def press_submit_button(self):
        try:
            self.driver.find_element(*locators.FINISH_BUTTON).click()
            WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locators.WAIT_FOR_CONF_MESSAGE))
        except NoSuchElementException:
            done_button = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locators.DONE_BUTTON_IN_EDIT_CERTIFICATES))
            done_button.click()
            WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locators.WAIT_FOR_CONF_MESSAGE_ON_EDIT))

    def click_on_checkbox_next_to_worker(self, index=0):
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.CHECKBOXES_NEXT_TO_WORKERS_IN_GRID))
        checkbox_in_grid = self.driver.find_elements(*locators.CHECKBOXES_NEXT_TO_WORKERS_IN_GRID)
        checkbox_in_grid[index].click()

    def click_on_archive_button(self):
        archive_button = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.ARCHIVE_BUTTON))
        archive_button.click()

    def click_on_archive_button_in_dialog(self):
        archive_button = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.ARCHIVE_BUTTON_IN_DIALOG))
        archive_button.click()
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.CONFIRMATION_MESSAGE_FOR_ARCH_WORKER))

    def click_edit_certificates_control(self):
        edit_certificates_control = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.EDIT_CERTIFICATES_CONTROL))
        edit_certificates_control.click()

    def click_save_team_button(self):
        save_team = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.SAVE_TEAM))
        save_team.click()

    def type_team_name_while_saving(self, team_name):
        save_team_name_field = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.SAVE_TEAM_NAME_FIELD))
        save_team_name_field.send_keys(team_name + Keys.ENTER)

    def click_save_button_while_saving_team(self):
        save_button = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.SAVE_BUTTON))
        save_button.click()

    def open_project_teams_filter(self):
        project_teams = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.PROJECT_TEAMS))
        project_teams.click()

    def mark_checkbox_in_modals(self, index=0):
        checkbox = self.driver.find_elements(*locators.PROJECT_TEAMS_CHECKBOXES)
        checkbox[index].click()

    def click_apply_button_in_modals(self):
        apply_button = self.driver.find_element(*locators.APPLY_BUTTON)
        apply_button.click()

    def verify_chips_is_present(self):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locators.UI_CHIPS))
            return True
        except NoSuchElementException:
            return False

    def select_all_workers_in_the_grid(self):
        select_all_checkbox = self.driver.find_element(*locators.SELECT_ALL_WORKERS)
        select_all_checkbox.click()

    def verify_text_of_counting_worker(self):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locators.COUNT_OF_SELECTED_WORKERS_IN_THE_GRID))
            return True
        except NoSuchElementException:
            return False









