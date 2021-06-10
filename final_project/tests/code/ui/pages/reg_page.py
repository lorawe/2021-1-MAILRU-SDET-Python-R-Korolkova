import allure

from ui.pages.base_page import BasePage
from ui.locators.pages_locators import RegistrationPageLocators
from ui.pages.main_page import MainPage


class RegistrationPage(BasePage):
    url = 'http://myapp:8085/reg'

    locators = RegistrationPageLocators()

    @allure.step('Register with {login}, {email}')
    def register(self, login, password, email):
        self.send(login, self.locators.INPUT_NAME)
        self.send(password, self.locators.INPUT_PASS)
        self.send(password, self.locators.INPUT_CONFIRM)
        self.send(email, self.locators.INPUT_EMAIL)
        self.click(self.locators.INPUT_TERM)
        self.click(self.locators.BUTTON_SUBMIT)
        return MainPage(self.driver)
