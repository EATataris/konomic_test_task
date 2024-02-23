from .base_page import BasePage
from .locators import RegistrationPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class RegistrationPage(BasePage):

    def test_invalid_username_formats(self):
        invalid_usernames = [
            '', #Пустое поле
            'user', #Слишком короткое имя пользователя
            'Useruseruseruseruseruseruseruseruseruser', #Слишком короткое имя пользователя
            '1username', #Имя пользователя начинается с цифры
            '_username', #Имя пользователя начинается с буквы
            'user1name', #Имя пользователя содержит цифру
            'usern@me', #Имя пользователя содержит символ не _
        ]

        shadow_host = self.browser.find_element(*RegistrationPageLocators.SHADOW_HOST)
        print('Shadow host element found')
        shadow_root = self.browser.execute_script('return arguments[0].shadowRoot', shadow_host)
        print('Switch to Shadow DOM')
        username_input = shadow_root.find_element(*RegistrationPageLocators.USERNAME_INPUT)
        submit_button = shadow_root.find_element(*RegistrationPageLocators.SUBMIT_BUTTON)

        for username in invalid_usernames:
            username_input.send_keys(username)
            self.click_element(submit_button)
            error_message = shadow_root.find_element(*RegistrationPageLocators.ERROR_TEXT)
            print(f'{error_message.text}')
            assert error_message, 'Сообщение об ошибке не найдено'
            username_input.send_keys([Keys.BACKSPACE] * 1000)
