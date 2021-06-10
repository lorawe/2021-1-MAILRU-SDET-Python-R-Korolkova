import allure

from ui.pages.base_page import BasePage
from ui.locators.pages_locators import MainPageLocators

class MainPage(BasePage):
    url = 'http://myapp:8085/welcome/'

    locators = MainPageLocators()
