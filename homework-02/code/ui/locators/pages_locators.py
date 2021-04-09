from selenium.webdriver.common.by import By


class BasePageLocators:
    BASE_PAGE_LOADED_LOCATOR = ''

    QUERY_LOCATOR = (By.NAME, 'q')
    GO_LOCATOR = (By.ID, 'submit')
    INPUT_SUBMIT_LOCATOR = (By.XPATH, "//input[@type='submit']")


class LoginPageLocators(BasePageLocators):
    COMPREHENSIONS = (By.XPATH, '//code/span[@class="comment" and contains(text(), "comprehensions")]')

    EVENTS_BUTTON = (By.XPATH, '//li[@id="events"]/a[@href="/events/"]')
    EVENTS_LINK_TEMPLATE = (By.XPATH, '//li[@id="events"]//a[@href="/events/{}"]')

    INTRODUCTION = (By.CSS_SELECTOR, 'div.introduction')
    LEARN_MORE_RELATIVE = (By.CSS_SELECTOR, 'a.readmore')

    MEMBERSHIP_DRIVE = (By.XPATH, '//a[@href="https://www.python.org/psf/membership/"]')

    LOGIN_HEAD_LOCATOR = (By.XPATH, "//div[contains(@class, 'responseHead-module-button')]")
    EMAIL_LOCATOR = (By.NAME, "email")
    PASSWORD_LOCATOR = (By.NAME, "password")
    LOGIN_BUTTON_LOCATOR = (By.XPATH, "//div[contains(@class,'authForm-module-button')]")
    USER_LOCATOR = (By.XPATH, "//div[contains(@class, 'right-module-userNameWrap')]")
    NOTIFY_EMAIL = (By.XPATH, "//div[contains(@class, 'notify-module-content') and contains(text(), 'Введите email')]")
    LOGIN = "machindz@mail.ru"
    PASSWORD = "abracadabra"


class PythonEventsPageLocators(BasePageLocators):
    EURO_PYTHON_2022 = (By.XPATH, '//a[contains(text(), "EuroPython 2022")]')
    LOCATION = (By.CLASS_NAME, 'single-event-location')


class DashboardPageLocators(BasePageLocators):
    DASHBOARD = (By.XPATH, "//a[@href = '/dashboard']")
    CAMPAIGN_NEW = (By.XPATH, "//a[@href = '/campaign/new']")
    CAMPAIGN_NEW_2 = (By.XPATH, "//div[contains(text(), 'Создать кампанию')]")
    SETTING_CAMPAIGN = (By.XPATH, "(//div[contains(@data-entity-type, 'campaign')])[2]")
    DELETE_LI = (By.XPATH, "//li[@title = 'Удалить']")
    SEGMENTS_LOCATOR = (By.XPATH, "//a[@href = '/segments']")
    PAGE_LOCATORS_TEMPLATE = (By.XPATH, "//a[@href = '/{}']")
    CAMPAIGN_CHECKBOX = (By.XPATH, "//div[contains(@data-entity-type,'campaign')]/label/input[@type='checkbox']")


class CampaignPageLocators(BasePageLocators):
    TRAFFIC = (By.XPATH, "//div[contains(text(), 'Трафик')]")
    TEASER = (By.XPATH, "//span[contains(text(), 'Тизер')]")
    INPUT_LINK = (By.XPATH, "//input[contains(@data-gtm-id,'ad_url_text')]")
    INPUT_FILE = (By.XPATH, "//input[@data-test='image_90x75']")
    INPUT_TITLE = (By.XPATH, "//input[@data-name='title_25']")
    INPUT_TEXT = (By.XPATH, "//textarea[@data-name='text_90']")
    SUBMIT_BUTTON = (By.XPATH, "//button[./div[contains(text(), 'Создать кампанию')]]")
    AD_URL = "ya.ru"
    FILE = "test.jpg"
    TITLE = "TitleText"
    TEXT = "TextText"


class SegmentsPageLocators(BasePageLocators):
    CREATE_SEGMENT_BUTTON = (By.XPATH, "//a[contains(@href,  '/segments/segments_list/new/')]")
    SEGMENT_APPS = (
        By.XPATH,
        "//div[contains(@class, 'adding-segments-modal__block-left')]/div[contains(text(), 'Приложения и игры')]")
    SEGMENT_APPS_CHECKBOX = (By.XPATH, "//input[contains(@class, 'adding-segments-source__checkbox')]")
    SUBMIT_BUTTON_ADD = (By.XPATH, "//button[./div[contains(text(), 'Добавить сегмент')]]")
    SUBMIT_BUTTON_CREATE = (By.XPATH, "//button[./div[contains(text(), 'Создать сегмент')]]")
    REMOVE_BUTTON = (By.XPATH, "//div[contains(@data-test, 'remove')]")
    INPUT_SEGMENT_TITLE = (By.XPATH, "//div[contains(@class, 'input_create-segment')]//input[contains(text(), '')]")
    SEGMENT_TABLE_TITLE = (By.XPATH, "//div[contains(@class, 'main-module-TableWrapper')]//a[contains(text(), '{}')]")
    BUTTON_CONFIRM_REMOVE = (By.XPATH, "//button[contains(@class, 'button_confirm-remove')]")
