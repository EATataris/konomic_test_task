import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def browser(request):
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()