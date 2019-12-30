from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.config_parser import Config
from src.pages.base_page import BasePage
from src.locators import login_locators as locators


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
        self.driver.find_element(*locators.LOGIN).click()
