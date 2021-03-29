import time

import pytest
from base import BaseCase
from ui.locators import basic_locators

class TestOne(BaseCase):
    @pytest.mark.UI("UI")
    def test_login(self):
        self.login("machindz@mail.ru", "abracadabra")
        assert basic_locators.DASHBOARD_URL in self.check_page()

    @pytest.mark.UI("UI")
    def test_logout(self):
        self.login("machindz@mail.ru", "abracadabra")
        self.click(basic_locators.RIGHTBUTTON_LOCATOR)
        self.click(basic_locators.LOGOUT_LOCATOR)
        self.driver.refresh()
        assert basic_locators.DASHBOARD_URL not in self.check_page()

    @pytest.mark.UI("UI")
    def test_edit_information(self):
        self.login("machindz@mail.ru", "abracadabra")
        self.click(basic_locators.PROFILE_LOCATOR)
        #if для избежания дублирования теста
        fio_input = "FIO"
        phone_input = "80987654321"
        if self.find(basic_locators.FIO_LOCATOR).text == fio_input or self.find(basic_locators.PHONE_LOCATOR).text == phone_input:
            fio_input = "FamiliaIO"
            phone_input = "80987654321"
        self.send(fio_input, basic_locators.FIO_LOCATOR)
        self.send(phone_input, basic_locators.PHONE_LOCATOR)
        self.click(basic_locators.SUBMIT_LOCATOR)
        assert self.check_visible(basic_locators.SUCCES_LOCATOR)
        self.driver.refresh()
        assert fio_input in self.find(basic_locators.USER_LOCATOR).text

    @pytest.mark.UI("UI")
    @pytest.mark.parametrize(
        'page_button, sub_url',
        [
            (
                basic_locators.SEGMENTS_LOCATOR, basic_locators.SEGMENTS_SUBURL
            ),
            (
                basic_locators.STATISTICS_LOCATOR, basic_locators.STATISTICS_SUBURL
            ),
        ]
    )
    def test_menu(self, page_button, sub_url):
        self.login("machindz@mail.ru", "abracadabra")
        self.click(page_button)
        assert sub_url in self.check_page()



