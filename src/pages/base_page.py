# -*- coding: utf-8 -*-
import time
import requests
import logging

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains

from src.locators import base_locators


class BasePage:
    """
    Base class to initialize the base page that will be called from all pages
    """

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 60

    def refresh_browser(self):
        self.driver.refresh()

    def get_current_url(self):
        return self.driver.current_url
