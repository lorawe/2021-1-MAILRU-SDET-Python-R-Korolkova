import logging
import os

import allure
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui.locators.pages_locators import BasePageLocators
from utils.decorators import wait

CLICK_RETRY = 3
BASE_TIMEOUT = 5

logger = logging.getLogger('test')


class PageNotLoadedException(Exception):
    pass


class BasePage(object):
    url = 'http://myapp:8085/'
    locators = BasePageLocators()

    def __init__(self, driver):
        self.driver = driver
        logger.info(f'{self.__class__.__name__} page is opening...')
        assert self.is_opened()

    def is_opened(self):
        def _check_url():
            if self.driver.current_url != self.url:
                raise PageNotLoadedException(
                    f'{self.url} did not opened in {BASE_TIMEOUT} for {self.__class__.__name__}. Current url: {self.driver.current_url}\n'
                    f'Current url: {self.driver.current_url}.')
            return True

        return wait(_check_url, error=PageNotLoadedException, check=True, timeout=BASE_TIMEOUT, interval=0.1)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def wait_missing(self, locator, timeout=None):
        return self.wait(timeout).until(EC.invisibility_of_element(locator))

    def scroll_to(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    @allure.step('Clicking {locator}')
    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            logger.info(f'Clicking on {locator}. Try {i + 1} of {CLICK_RETRY}...')
            try:
                element = self.find(locator, timeout=timeout)
                self.scroll_to(element)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    @allure.step('Send {keys} to {locator}')
    def send(self, keys, locator):
        self.find(locator).clear()
        self.find(locator).send_keys(keys)
