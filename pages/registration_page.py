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
            error_message = self.switch_to_shadow_dom().find_element(*RegistrationPageLocators.USERNAME_ERROR_TEXT)
            print(f'{error_message.text}')
            assert error_message, 'Формат username верный!'
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
            error_message = self.switch_to_shadow_dom().find_element(*RegistrationPageLocators.EMAIL_ERROR_TEXT)
            print(f'{error_message.text}')
            assert error_message, 'Формат email верный!'
            email_input.send_keys([Keys.BACKSPACE] * 1000)

    def test_invalid_password_format(self):
        invalid_passwords = [
            "",  # Пустой пароль
            "short",  # Слишком короткий пароль
            "a" * 65,  # Слишком длинный пароль
            "no_digit_or_uppercase",  # Пароль без цифры и заглавной буквы
            "NOLOWER123",  # Пароль без прописных букв, но с цифррами
            "noupper123",  # Пароль без заглавной буквы, но с цифрами
            "Password$",  # Пароль с символам заглавной, прописной, но без цифры
            "@@@@$$$$123", # Пароль с символам, цифрами, но без букв
            "@@@@$$$$123A",  # Пароль с символам, цифрами, и заглавной буквой
            "@@@@$$$$123a",  # Пароль с символам, цифрами, и прописной буквой
            "12345677890", # Пароль только с цифрами
            "12345678Йй", # Пароль с цифрами, заглавной, прописной буквой кириллицей
        ]

        password_input = self.switch_to_shadow_dom().find_element(*RegistrationPageLocators.PASSWORD_INPUT)
        submit_button = self.switch_to_shadow_dom().find_element(*RegistrationPageLocators.SUBMIT_BUTTON)
        password_show_button = self.switch_to_shadow_dom().find_element(*RegistrationPageLocators.PASSWORD_SHOW_BUTTON)
        self.click_element(password_show_button)

        for password in invalid_passwords:
            password_input.send_keys(password)
            self.click_element(submit_button)
            error_message = self.switch_to_shadow_dom().find_element(*RegistrationPageLocators.PASSWORD_ERROR_TEXT)
            print(f'{error_message.text}')
            assert error_message, 'Формат пароля верный!'
            password_input.send_keys([Keys.BACKSPACE] * 1000)

    def test_invalid_referral_code_format(self):
        invalid_codes = [
            "", #Пустой код
            "123", #Слишком короткий код
            "code1234@", #Слишком длинный код
        ]

        referral_input = self.switch_to_shadow_dom().find_element(*RegistrationPageLocators.REFERRAL_INPUT)
        submit_button = self.switch_to_shadow_dom().find_element(*RegistrationPageLocators.SUBMIT_BUTTON)

        for code in invalid_codes:
            referral_input.send_keys(code)
            if not submit_button.is_enabled():
                error_message = self.switch_to_shadow_dom().find_element(*RegistrationPageLocators.REFERRAL_ERROR_TEXT)
                print(f'{error_message.text}')
                referral_input.send_keys([Keys.BACKSPACE] * 1000)
            else:
                assert 'Формат реферального кода верный!'