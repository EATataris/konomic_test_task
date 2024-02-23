from .base_page import BasePage
from .locators import RegistrationPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class RegistrationPage(BasePage):
    def switch_to_shadow_dom(self):
        shadow_host = self.browser.find_element(*RegistrationPageLocators.SHADOW_HOST)
        shadow_root = self.browser.execute_script('return arguments[0].shadowRoot', shadow_host)
        return shadow_root
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

        username_input = self.switch_to_shadow_dom().find_element(*RegistrationPageLocators.USERNAME_INPUT)
        submit_button = self.switch_to_shadow_dom().find_element(*RegistrationPageLocators.SUBMIT_BUTTON)

        for username in invalid_usernames:
            username_input.send_keys(username)
            self.click_element(submit_button)
            error_message = self.switch_to_shadow_dom().find_element(*RegistrationPageLocators.ERROR_TEXT)
            print(f'{error_message.text}')
            assert error_message, 'Сообщение об ошибке не найдено'
            username_input.send_keys([Keys.BACKSPACE] * 1000)

    def test_invalid_email_formats(self):
        invalid_emails = [
            "",  # Пустой email
            "invalid",  # Некорректный формат
            "user@",  # Недостаточно символов после '@'
            "@domain.com",  # Отсутствие имени пользователя
            "user@domain",  # Отсутствие домена
            "user@domain.",  # Отсутствие домена после точки
            "user@domain.com@",  # Лишние символы после точки
            "user@domain!.com",  # Недопустимые символы
        ]

        email_input = self.switch_to_shadow_dom().find_element(*RegistrationPageLocators.EMAIL_INPUT)
        submit_button = self.switch_to_shadow_dom().find_element(*RegistrationPageLocators.SUBMIT_BUTTON)

        for email in invalid_emails:
            email_input.send_keys(email)
            self.click_element(submit_button)
            error_message = self.switch_to_shadow_dom().find_element(*RegistrationPageLocators.ERROR_TEXT)
            print(f'{error_message.text}')
            assert error_message, 'Сообщение об ошибке не найдено'
            email_input.send_keys([Keys.BACKSPACE] * 1000)