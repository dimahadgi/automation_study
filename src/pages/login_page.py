from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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
        login_button = self.driver.find_element(*locators.LOGIN)
        login_button.click()
        check_login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locators.GRID))
        if len(check_login_button.id) <= 0:
            print("login button is not pressed, clicking second time")
            self.driver.find_element(*locators.LOGIN).click()
            time.sleep(606)
