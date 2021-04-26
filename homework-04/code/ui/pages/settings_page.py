from ui.pages.base_page import BasePage
from ui.locators.locators_android import SettingsPageANDROIDLocators
import allure


class SettingsPage(BasePage):
    def click_on_news_source_button(self):
        pass

    def click_on_news_source(self, source):
        pass

    def check_news_source(self):
        pass

    def click_on_source_back_button(self):
        pass

    def click_on_settings_back_button(self):
        pass


class SettingsPageANDROID(SettingsPage):
    locators = SettingsPageANDROIDLocators()

    @allure.step("Нажимаем на кнопку выбора источника новостей")
    def click_on_news_source_button(self):
        self.swipe_to_element(self.locators.NEWS_SOURCE_BUTTON, 5)
        self.click_for_android(self.locators.NEWS_SOURCE_BUTTON)

    @allure.step("Нажимаем на источник новостей")
    def click_on_news_source(self, source):
        source_locator = (self.locators.NEWS_SOURCE[0],
                          self.locators.NEWS_SOURCE[1].format(source))
        self.click_for_android(source_locator)

    @allure.step("Проверяем галочку у выбранного источника новостей")
    def check_news_source(self):
        self.find(self.locators.MARK)

    @allure.step("Нажимаем на кнопку назад")
    def click_on_source_back_button(self):
        self.click_for_android(self.locators.TOOLBAR_SOURCES_BACK_BUTTON)

    @allure.step("Нажимаем на кнопку назад")
    def click_on_settings_back_button(self):
        self.click_for_android(self.locators.TOOLBAR_SETTINGS_BACK_BUTTON)
