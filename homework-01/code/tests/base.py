import time

import pytest
from ui.locators import basic_locators
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseCase:
    driver = None
    config = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config):
        self.driver = driver
        self.config = config

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        element.click()

    def check_visible(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

    def check_page(self):
        return self.driver.current_url

    def send(self, keys, locator):
        self.find(locator).clear()
        self.find(locator).send_keys(keys)


    def login(self, login, password):
        self.click(basic_locators.INPUT_HEAD_LOCATOR)
        self.send(login, basic_locators.EMAIL_LOCATOR)
        self.send(password, basic_locators.PASSWORD_LOCATOR)
        self.click(basic_locators.INPUT_FORM_LOCATOR)
