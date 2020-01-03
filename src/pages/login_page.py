from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from retrying import retry

from src.pages.base_page import BasePage
from src.locators import login_locators as locators
import time


class LoginPage(BasePage):
    def specify_email(self, email):
        login_field = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.EMAIL))
        login_field.send_keys(email)

    def specify_pass(self, password):
        pwd_field = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.PASSWORD))
        pwd_field.send_keys(password)

    def press_login(self):
        def wait_for_grid():
            WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locators.GRID))

        @retry(retry_on_exception=wait_for_grid)
        def click_on_login_button():
            login_button = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locators.LOGIN))
            login_button.click()
            try:
                wait_for_grid()
            except TimeoutException:
                click_on_login_button()

        click_on_login_button()






