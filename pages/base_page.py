from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def click_element(self, locator):
        print(f"Clicking element: {locator}")
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator)).click()

    def open(self):
        self.browser.get(self.url)

