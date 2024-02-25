from .base_page import BasePage
from .locators import KoshelekPageLocators


class KoshelekPage(BasePage):

    def go_to_registration_page(self):
        print('Going to registration page')
        self.click_element(KoshelekPageLocators.REGISTRATION_LINK)
