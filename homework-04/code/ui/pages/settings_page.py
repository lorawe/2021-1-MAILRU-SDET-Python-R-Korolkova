from ui.pages.base_page import BasePage
from ui.locators.locators_android import SettingsPageANDROIDLocators
import allure


class SettingsPage(BasePage):
    def click_on_news_source_button(self):
        pass

    def click_on_news_source(self, source):
        pass

    def click_on_about_button(self):
        pass

    def check_news_source(self):
        pass

    def click_on_source_back_button(self):
        pass

    def click_on_settings_back_button(self):
        pass

    def set_news_source(self, source):
        pass

    def go_back_to_main(self, pressing):
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

    @allure.step("Устанавливаем источник новостей")
    def set_news_source(self, source):
        self.click_on_news_source_button()
        self.click_on_news_source(source)
        self.check_news_source()

    @allure.step("Возвращаемся на главную страницу со страницы настроек")
    def go_back_to_main(self, pressing):
        for i in range(pressing):
            self.click_on_source_back_button()

    @allure.step("Переходим на страницу 'О Приложении'")
    def click_on_about_button(self):
        self.swipe_to_element(self.locators.ABOUT_BUTTON, 3)
        self.click_for_android(self.locators.ABOUT_BUTTON)
