from selenium.webdriver.common.by import By


class BasePageLocators:

    BUTTON_SUBMIT = (By.ID, 'submit')


class LoginPageLocators(BasePageLocators):
    INPUT_NAME = (By.ID, 'username')
    INPUT_PASS = (By.ID, 'password')
    NOTIFY_INVALID = (By.ID, 'flash')
    BUTTON_REG = (By.XPATH, "//a[@href='/reg']")


class MainPageLocators(BasePageLocators):
    BUTTON_LOGOUT = (By.ID, 'logout')


class RegistrationPageLocators(BasePageLocators):
    INPUT_NAME = (By.ID, 'username')
    INPUT_PASS = (By.ID, 'password')
    INPUT_CONFIRM = (By.ID, 'confirm')
    INPUT_EMAIL = (By.ID, 'email')
    INPUT_TERM = (By.ID, 'term')
