import pytest
from marussia_tests.base import BaseCase


class TestMarussiaAndroid(BaseCase):

    @pytest.mark.AndroidUI
    def test_search_text(self):
        self.main_page.click_on_deny_buttons()
        self.main_page.click_on_keyboard_button()
        self.main_page.enter_value_in_search_field('Russia')
        self.main_page.check_dialog_title('Россия')
        self.main_page.check_number('численность')
        self.main_page.check_dialog_title('146 млн.')

    @pytest.mark.AndroidUI
    def test_search_calculator(self):
        self.main_page.click_on_deny_buttons()
        self.main_page.click_on_keyboard_button()
        self.main_page.enter_value_in_search_field('5+3')
        self.main_page.check_dialog_text('8')

    @pytest.mark.AndroidUI
    def test_news_source(self):
        source = 'Вести FM'
        self.main_page.click_on_deny_buttons()
        self.main_page.click_on_menu_button()
        self.settings_page.set_news_source(source)
        self.settings_page.go_back_to_main()
        self.main_page.check_news_source(source)

    @pytest.mark.AndroidUI
    def test_copyrighting(self):
        version = "1.39.1"
        copyrighting_str = "Все права защищены"
        self.main_page.click_on_deny_buttons()
        self.main_page.click_on_menu_button()
        self.settings_page.click_on_about_button()
        self.about_page.check_version(version)
        self.about_page.check_copyright(copyrighting_str)
