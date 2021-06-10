import datetime
from random import randrange

import allure
import pytest

from tests.base import BaseCase
from ui.pages.reg_page import RegistrationPage


class TestLogin(BaseCase):

    """
    Тест проверяет авторизацию с верным логином и паролем. Сначала переходит на login страницу,
    затем вводит данные в нужные поля, нажимает кнопку авторизации и проверяет, что открылась главная страница.
    """
    @pytest.mark.UI
    @allure.epic('Myapp test')
    @allure.feature('UI tests')
    @allure.story('Login test')
    @allure.testcase("http://myapp")
    @allure.description("Testing of authorization with correct login and correct password on Login Page.")
    def test_right_login(self):
        main_page = self.login_page.login("testuser", "1234567890")
        main_page.is_opened()

    """
    Тест проверяет авторизацию с неверным логином, но верным паролем. Сначала переходит на login страницу, 
    затем вводит данные в нужные поля, нажимает кнопку авторизации и проверяет, что главная страница не открыта.
    Затем проверяется уведомление о невалидных данных.
    """
    @pytest.mark.UI
    @allure.epic('Myapp test')
    @allure.feature('UI tests')
    @allure.story('Login test')
    @allure.testcase("http://myapp")
    @allure.description("Testing of authorization with incorrect login and correct password on Login Page.")
    def test_wrong_login(self):
        with pytest.raises(TimeoutError) as exc_info:
            main_page = self.login_page.login("gdfsg5325125423", "1234567890")
            main_page.is_opened()
        self.login_page.check_notify_email()

    """
        Тест проверяет авторизацию с верным логином но неверным паролем. Сначала переходит на login страницу, 
        затем вводит данные в нужные поля, нажимает кнопку авторизации и проверяет что главная страница не открыта.
        Затем проверяется уведомление о невалидных данных.
    """
    @pytest.mark.UI
    @allure.epic('Myapp test')
    @allure.feature('UI tests')
    @allure.story('Login test')
    @allure.testcase("http://myapp")
    @allure.description("Testing of authorization with correct login and incorrect password on Login Page.")
    def test_wrong_password(self):
        with pytest.raises(TimeoutError) as exc_info:
            main_page = self.login_page.login("testuser", "46457257abracadabra")
            main_page.is_opened()
        self.login_page.check_notify_email()


class TestRegistration(BaseCase):
    """
        Тест проверяет регистрацию с валидными логином и паролем. Сначала переходит на login страницу, затем на reg,
        затем вводит данные в нужные поля, нажимает кнопку регистрации и проверяет, что открылась главная страница.
    """

    @pytest.mark.UI
    @allure.epic('Myapp test')
    @allure.feature('UI tests')
    @allure.story('Registration test')
    @allure.testcase("http://myapp")
    @allure.description("Testing of registration with correct login and correct password on Registration Page.")
    def test_registration_valid(self):
        reg_page = self.login_page.go_to_reg_page()
        reg_page.is_opened()
        now = datetime.datetime.now()
        rand = randrange(100)
        user = f'testuser{now.hour}{now.minute}{rand}'
        main_page = reg_page.register(user, '1234567890', f'{user}@mail.ru')
        main_page.is_opened()
