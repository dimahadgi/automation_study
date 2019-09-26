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

