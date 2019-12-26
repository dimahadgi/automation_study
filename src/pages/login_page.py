import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.pages.base_page import BasePage
from src.locators import login_locators as locators


class LoginPage(BasePage):

    def specify_email(self, text):
        login_field = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.EMAIL)
        )
        login_field.send_keys(text)

    def specify_pass(self, text):
        pwd_field = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locators.PASSWORD)
        )
        pwd_field.send_keys(text)

    def click_forgot(self):
        pass

    def press_login(self):
        def click_login():
            login_button = self.driver.find_element(*locators.LOGIN)
            login_button.click()
        try:
            click_login()
        except:
            time.sleep(3)
            click_login()

