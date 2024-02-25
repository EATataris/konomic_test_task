from .pages.koshelek_page import KoshelekPage
from .pages.registration_page import RegistrationPage

import time


def test_run(browser):
    # link = "https://koshelek.ru/"
    link = "https://exchange.konomik.com/"
    page = KoshelekPage(browser, link)
    page.open()
    page.go_to_registration_page()
    time.sleep(3)
    registration_page = RegistrationPage(browser, browser.current_url)
    registration_page.test_invalid_username_formats()
    registration_page.test_invalid_email_formats()
    registration_page.test_invalid_password_format()
    registration_page.test_invalid_referral_code_format()
    registration_page.text_user_agreement_checkbox_not_checked()