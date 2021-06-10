import allure

from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.locators.pages_locators import LoginPageLocators
from ui.pages.reg_page import RegistrationPage


class LoginPage(BasePage):
    url = 'http://myapp:8085/'

    locators = LoginPageLocators()

    @allure.step('Login as {login}')
    def login(self, login, password):
        self.send(login, self.locators.INPUT_NAME)
        self.send(password, self.locators.INPUT_PASS)
        self.click(self.locators.BUTTON_SUBMIT)
        return MainPage(self.driver)

    @allure.step('Check invalid login notify')
    def check_notify_email(self):
        assert self.find(self.locators.NOTIFY_INVALID)

    @allure.step("Go to registration page")
    def go_to_reg_page(self):
        self.click(self.locators.BUTTON_REG)
        return RegistrationPage(self.driver)
