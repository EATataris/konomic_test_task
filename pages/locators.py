from selenium.webdriver.common.by import By


class KoshelekPageLocators():
    REGISTRATION_LINK = (By.XPATH, '//a[@href="/authorization/signup"]')


class RegistrationPageLocators():
    SHADOW_HOST = (By.CSS_SELECTOR, '.remoteComponent')

    USERNAME_INPUT = (By.CSS_SELECTOR, 'div[data-wi="user-name"] input')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'div[data-wi="identificator"] input')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'div[data-wi="password"] input')
    REFERRAL_INPUT = (By.CSS_SELECTOR, 'div[data-wi="referral"] input')

    PASSWORD_SHOW_BUTTON = (By.CSS_SELECTOR, 'div[data-wi="password"] button')

    USERNAME_ERROR_TEXT = (By.CSS_SELECTOR, 'div[data-wi="user-name"] span')
    EMAIL_ERROR_TEXT = (By.CSS_SELECTOR, 'div[data-wi="identificator"] span')
    PASSWORD_ERROR_TEXT = (By.CSS_SELECTOR, 'div[data-wi="password"] span')
    REFERRAL_ERROR_TEXT = (By.CSS_SELECTOR, 'div[data-wi="referral"] span')

    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'div[data-wi="submit-button"] button')


