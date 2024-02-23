from .pages.koshelek_page import KoshelekPage
from .pages.registration_page import RegistrationPage

import time


def test_run(browser):
    link = "https://koshelek.ru/"
    page = KoshelekPage(browser, link)
    page.open()
    page.go_to_registration_page()
    time.sleep(3)
    registration_page = RegistrationPage(browser, browser.current_url)
    registration_page.test_invalid_username_too_short()
    time.sleep(3)
    registration_page.test_invalid_username_too_long()
    time.sleep(1)