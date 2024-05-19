import pytest
from selene import browser, be, have
from selenium import webdriver


@pytest.fixture(scope="function")
def open_browser(chose_size_of_screen):
    browser.config.base_url = 'https://demoqa.com'
    driver = webdriver.FirefoxOptions()
    # driver_options.add_argument('--headless')
    browser.config.driver_options = driver
    browser.config.type_by_js = True
    print("this is beginning of fixture - set up")
    yield
    browser.quit()
    print("end of fixture - tear down")


@pytest.fixture(scope="function")
def chose_size_of_screen():
    browser.config.window_height = 2000
    browser.config.window_width = 2000
    print("prepare screen size - set up")
