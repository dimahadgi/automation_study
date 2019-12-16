from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

from src.pages.base_page import BasePage
from src.locators import main_page_locators as locators


class MainPage(BasePage):

    def specify_search(self, text):
        search_field = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.SEARCH)
        )
        search_field.send_keys(text)

    def press_add_new_worker(self):
        add_new_worker = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.ADD_NEW_WORKER)
        )
        add_new_worker.click()

    def enter_email_address(self, email):
        enter_email = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.EMAIL_ADDRESS_FIELD)
        )
        enter_email.send_keys(email)

    def press_search_emails(self):
        press_search = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.SEARCH_EMAILS_BUTTON)
        )
        press_search.click()

    def enter_first_name(self, name):
        enter_first_name = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.FIRST_NAME_FIELD)
        )
        enter_first_name.send_keys(name)

    def enter_last_name(self, name):
        enter_last_name = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.LAST_NAME_FIELD)
        )
        enter_last_name.send_keys(name)

    def press_create_button(self):
        press_create = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.CREATE_WORKER_BUTTON)
        )
        press_create.click()

    def wait_for_confirm_message(self):
        check_element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.CONFIRMATION_MESSAGE)
        )


