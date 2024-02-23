from .base_page import BasePage
from .locators import KoshelekPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class KoshelekPage(BasePage):

    def go_to_registration_page(self):
        print('Going to registration page')
        self.click_element(KoshelekPageLocators.REGISTRATION_LINK)
