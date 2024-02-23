from selenium.webdriver.common.by import By


class KoshelekPageLocators():
    REGISTRATION_LINK = (By.XPATH, '//a[@href="/authorization/signup"]')


class RegistrationPageLocators():
    SHADOW_HOST = (By.CSS_SELECTOR, '.remoteComponent')
    USERNAME_INPUT = (By.CSS_SELECTOR, '.v-text-field__slot > input')
    ERROR_TEXT = (By.CSS_SELECTOR, 'span[class="k-text"]:first-child')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'div[data-wi="submit-button"] > button')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#username')

