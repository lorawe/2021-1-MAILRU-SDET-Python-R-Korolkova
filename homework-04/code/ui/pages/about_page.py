import allure
import fnmatch
import os

from ui.pages.base_page import BasePage
from ui.locators.locators_android import AboutPageANDROIDLocators


class AboutPage(BasePage):
    def check_version(self):
        pass

    def check_copyright(self, copyright_str):
        pass


class AboutPageANDROID(AboutPage):
    locators = AboutPageANDROIDLocators()

    @allure.step("Проверяем версию приложения")
    def check_version(self):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path_apk = os.path.normpath(os.path.join(current_dir, f'../../stuff/'))
        apk_name = [f for f in os.listdir(file_path_apk) if fnmatch.fnmatch(f, '*.apk')][0]
        version = apk_name[apk_name.find("v") + 1: apk_name.find(".apk")]
        assert version in self.find(self.locators.VERSION).text

    @allure.step("Проверяем права использования")
    def check_copyright(self, copyright_str):
        assert copyright_str in self.find(self.locators.COPYRIGHTING).text
