import allure
import pytest

from base_tests.base import BaseCase


class TestLogin(BaseCase):
    @pytest.mark.UI
    @allure.epic('Mail target.my.com test')
    @allure.feature('UI tests')
    @allure.story('Login test')
    @allure.testcase("https://mail.ru")
    @allure.description("Testing of authorization with incorrect login and correct password on Login Page.")
    def test_wrong_login(self):
        with pytest.raises(TimeoutError) as exc_info:
            dashboard_page = self.login_page.login("gdfsg5325125423", "abracadabra")
            dashboard_page.is_opened()
        self.login_page.check_notify_email()

    @pytest.mark.UI
    @allure.epic('Mail target.my.com test')
    @allure.feature('UI tests')
    @allure.story('Login test')
    @allure.testcase("https://mail.ru")
    @allure.description("Testing of authorization with correct login and incorrect password on Login Page.")
    def test_wrong_password(self):
        with pytest.raises(TimeoutError) as exc_info:
            dashboard_page = self.login_page.login("machindz@mail.ru", "46457257abracadabra")
            dashboard_page.is_opened()


@pytest.mark.UI
class TestCampaign(BaseCase):
    @pytest.mark.UI
    @allure.epic('Mail target.my.com test')
    @allure.feature('UI tests')
    @allure.story('Campaign page test')
    @allure.testcase("https://mail.ru")
    @allure.description("Testing of create campaign on campaign page.")
    def test_create_campaign(self, login):
        dashboard_page = login
        campaign_page = dashboard_page.go_to_campaign()
        campaign_page.create_campaign()
        dashboard_page.check_campaign()


class TestSegments(BaseCase):
    @pytest.mark.UI
    @allure.epic('Mail target.my.com test')
    @allure.feature('UI tests')
    @allure.story('Segments page test')
    @allure.testcase("https://mail.ru")
    @allure.description("Testing of create segments on segment page.")
    def test_create_segment(self, login):
        dashboard_page = login
        segments_page = dashboard_page.go_to_segments()
        new_segment_title = segments_page.create_segment()
        segments_page.check_segment(new_segment_title)

    @pytest.mark.UI
    @allure.epic('Mail target.my.com test')
    @allure.feature('UI tests')
    @allure.story('Segments page test')
    @allure.testcase("https://mail.ru")
    @allure.description("Testing of delete segments on segment page.")
    def test_delete_segment(self, login):
        dashboard_page = login
        segments_page = dashboard_page.go_to_segments()
        new_segment_title = segments_page.create_segment()
        segments_page.check_segment(new_segment_title)
        segments_page.delete_segment()
        segments_page.check_deleted_segment(new_segment_title)
