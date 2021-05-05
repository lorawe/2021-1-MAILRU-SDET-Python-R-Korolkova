from ui.pages.base_page import BasePage
from ui.locators.locators_android import MainPageANDROIDLocators
import allure


class MainPage(BasePage):
    def click_on_deny_buttons(self):
        pass

    def click_on_keyboard_button(self):
        pass

    def enter_value_in_search_field(self, text):
        pass

    def check_dialog_title(self, title):
        pass

    def check_dialog_text(self, text):
        pass

    def click_on_menu_button(self):
        pass

    def check_number(self, suggest):
        pass

    def check_news_source(self, source):
        pass


class MainPageANDROID(MainPage):
    locators = MainPageANDROIDLocators()

    @allure.step("Отклоняем разрешения")
    def click_on_deny_buttons(self):
        self.click_for_android(self.locators.DENY_BUTTON)
        self.click_for_android(self.locators.DENY_BUTTON)

    @allure.step("Нажимаем на кнопку клавиатуры-поиска")
    def click_on_keyboard_button(self):
        self.click_for_android(self.locators.KEYBOARD)

    @allure.step("Вводим значение в поле поиска")
    def enter_value_in_search_field(self, text):
        self.find(self.locators.SEARCH_FIELD).send_keys(text)
        self.driver.hide_keyboard()
        self.click_for_android(self.locators.INPUT_ACTION)

    @allure.step("Проверяем заголовок диалога")
    def check_dialog_title(self, title):
        title_locator = (self.locators.DIALOG_CARD_TITLE[0],
                           self.locators.DIALOG_CARD_TITLE[1].format(title))
        assert self.find(title_locator)

    @allure.step("Проверяем текст диалога")
    def check_dialog_text(self, text):
        dialog_locator = (self.locators.DIALOG_ITEM[0],
                         self.locators.DIALOG_ITEM[1].format(text))
        assert self.find(dialog_locator)

    @allure.step("Нажимаем на кнопку меню")
    def click_on_menu_button(self):
        self.click_for_android(self.locators.MENU)

    @allure.step("Проверяем численность")
    def check_number(self, suggest):
        suggest_locator = (self.locators.SUGGEST_ITEM[0],
                          self.locators.SUGGEST_ITEM[1].format(suggest))
        self.swipe_to_element(suggest_locator, 2)
        self.click_for_android(suggest_locator)

    @allure.step("Проверяем источник новостей")
    def check_news_source(self, source):
        self.click_on_keyboard_button()
        self.enter_value_in_search_field('News')
        self.check_dialog_text(source)
