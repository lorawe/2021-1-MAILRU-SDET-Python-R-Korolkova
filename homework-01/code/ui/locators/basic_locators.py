from selenium.webdriver.common.by import By

INPUT_HEAD_LOCATOR = (By.XPATH, "//div[contains(@class, 'responseHead-module-button-1BMAy4')]")
EMAIL_LOCATOR = (By.NAME, "email")
PASSWORD_LOCATOR = (By.NAME, "password")
# INPUT_FORM_LOCATOR = (By.CLASS_NAME, "authForm-module-button-2G6lZu")
INPUT_FORM_LOCATOR = (By.XPATH, "//*[@class='authForm-module-button-2G6lZu']")
USER_LOCATOR = (By.XPATH, "//div[contains(@class, 'right-module-userNameWrap-34ibLS')]")
DASHBOARD_URL = "target.my.com/dashboard"
#RIGHTBUTTON_LOCATOR = (By.XPATH, "//div[contains(@class, 'right-module-rightButton')]")
RIGHTBUTTON_LOCATOR = (By.XPATH, "//div[contains(@class, 'right-module-rightWrap')]")
LOGOUT_LOCATOR = (By.XPATH, "//ul[contains(@class, 'rightMenu')]//a[contains(text(), 'Выйти')]")
RIGHTMODULE_LOCATOR = (By.XPATH, "//div[contains(@class, 'right-module-rightWrap')]")
PROFILE_LOCATOR = (By.XPATH, "//a[@href = '/profile']")
SEGMENTS_LOCATOR = (By.XPATH, "//a[@href = '/segments']")
SEGMENTS_SUBURL = "target.my.com/segments"
STATISTICS_LOCATOR = (By.XPATH, "//a[@href = '/statistics']")
STATISTICS_SUBURL = "target.my.com/statistics"
FIO_LOCATOR = (By.XPATH, "//div[contains(@data-name, 'fio')]//input")
PHONE_LOCATOR = (By.XPATH, "//div[contains(@data-name, 'phone')]//input")
PROFILEMAIL_LOCATOR = (By.XPATH, "//div[contains(@data-name, 'mail')]//input")
SUBMIT_LOCATOR = (By.XPATH, "//button[contains(@data-class-name, 'Submit')]")
SUCCES_LOCATOR = (By.XPATH, "//*[contains(text(), 'Информация успешно сохранена')]")


