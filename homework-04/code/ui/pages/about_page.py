import allure

from ui.pages.base_page import BasePage
from ui.locators.locators_android import AboutPageANDROIDLocators


class AboutPage(BasePage):
    def check_version(self, version):
        pass

    def check_copyright(self, copyright_str):
        pass

class AboutPageANDROID(AboutPage):
    locators = AboutPageANDROIDLocators()

    @allure.step("Проверяем версию приложения")
    def check_version(self, version):
        assert version in self.find(self.locators.VERSION).text

    @allure.step("Проверяем права использования")
    def check_copyright(self, copyright_str):
        assert copyright_str in self.find(self.locators.COPYRIGHTING).text

