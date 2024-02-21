from .base_page import BasePage
from .locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    def test_invalid_username_too_short(self):
        shadow_host = self.browser.find_element(*RegistrationPageLocators.SHADOW_HOST)
        print('Shadow host element finded')
        shadow_root = self.browser.execute_script('return arguments[0].shadowRoot', shadow_host)
        print('Switch to Shadow DOM')
        username_input = shadow_root.find_element(*RegistrationPageLocators.USERNAME_INPUT)
        username_input.send_keys('user')
        submit_button = shadow_root.find_element(*RegistrationPageLocators.SUBMIT_BUTTON)
        self.click_element(submit_button)
        error_message = shadow_root.find_element(*RegistrationPageLocators.ERROR_TEXT)
        print(f'{error_message.text}')
        assert error_message, 'Сообщение об ошибке не найдено'
