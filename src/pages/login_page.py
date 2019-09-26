from src.pages.base_page import BasePage
from src.locators import login_locators as locators


from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class LoginPage(BasePage):

    def specify_email(self, text):
        login_field = self.driver.find_element(*locators.EMAIL)
        login_field.send_keys(text)

    def specify_pass(self, text):
        pwd_field = self.driver.find_element(*locators.PASSWORD)
        pwd_field.send_keys(text)

    def click_forgot(self):
        pass

    def press_login(self):
        login_button = self.driver.find_element(*locators.LOGIN)
        login_button.click()
