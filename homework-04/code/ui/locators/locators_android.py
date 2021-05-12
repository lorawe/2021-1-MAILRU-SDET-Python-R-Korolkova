from appium.webdriver.common.mobileby import MobileBy


class BasePageANDROIDLocators:
    pass


class MainPageANDROIDLocators(BasePageANDROIDLocators):
    DENY_BUTTON = (MobileBy.ID, 'com.android.packageinstaller:id/permission_deny_button')
    KEYBOARD = (MobileBy.ID, 'ru.mail.search.electroscope:id/keyboard')
    SEARCH_FIELD = (MobileBy.ID, 'ru.mail.search.electroscope:id/input_text')
    INPUT_ACTION = (MobileBy.ID, 'ru.mail.search.electroscope:id/text_input_action')
    DIALOG_CARD_TITLE = (MobileBy.XPATH, "//android.widget.TextView[contains(@text, '{}')]")
    SUGGEST_ITEM = (MobileBy.XPATH, "//android.widget.TextView[contains(@text, '{}')]")
    DIALOG_ITEM = (MobileBy.XPATH, "//android.widget.TextView[contains(@text, '{}')]")
    MENU = (MobileBy.ID, 'ru.mail.search.electroscope:id/assistant_menu_bottom')

class SettingsPageANDROIDLocators(BasePageANDROIDLocators):
    NEWS_SOURCE_BUTTON = (MobileBy.ID, 'ru.mail.search.electroscope:id/user_settings_field_news_sources')
    NEWS_SOURCE = (MobileBy.XPATH, "//android.widget.TextView[contains(@text, '{}')]")
    MARK = (MobileBy.ID, 'ru.mail.search.electroscope:id/news_sources_item_selected')
    TOOLBAR_SOURCES_BACK_BUTTON = (MobileBy.XPATH,
                           "//android.widget.LinearLayout//android.widget.ImageButton")
    TOOLBAR_SETTINGS_BACK_BUTTON = (MobileBy.XPATH,
                                   "//android.widget.LinearLayout[contains(@id, 'ru.mail.search.electroscope:id/user_settings_toolbar')]//android.widget.ImageButton")
    ABOUT_BUTTON = (MobileBy.ID, "ru.mail.search.electroscope:id/user_settings_about")

class AboutPageANDROIDLocators(BasePageANDROIDLocators):
    VERSION = (MobileBy.ID, "ru.mail.search.electroscope:id/about_version")
    COPYRIGHTING = (MobileBy.ID, "ru.mail.search.electroscope:id/about_copyright")