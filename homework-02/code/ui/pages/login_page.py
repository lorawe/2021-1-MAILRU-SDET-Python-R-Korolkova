import allure

from ui.pages.base_page import BasePage
from ui.locators.pages_locators import LoginPageLocators
from ui.pages.dashboard_page import DashboardPage

class LoginPage(BasePage):
    url = 'https://target.my.com/'

    locators = LoginPageLocators()

    @allure.step('Login as {login}')
    def login(self, login, password):
        self.click(self.locators.LOGIN_HEAD_LOCATOR)
        self.send(login, self.locators.EMAIL_LOCATOR)
        self.send(password, self.locators.PASSWORD_LOCATOR)
        self.click(self.locators.LOGIN_BUTTON_LOCATOR)
        return DashboardPage(self.driver)

    @allure.step('Check notify email')
    def check_notify_email(self):
        assert self.find(self.locators.NOTIFY_EMAIL)

