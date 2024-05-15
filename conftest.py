import pytest
from selene import browser, be, have

@pytest.fixture(scope="function")
def open_browser(chose_size_of_screen):
        browser.open('https://kpditmo.ru/login/index.php')
        print("this is beginning of fixture - set up")
        yield
        browser.quit()
        print("end of fixture - tear down")
@pytest.fixture(scope="function")
def chose_size_of_screen():
        browser.config.window_height =2000
        browser.config.window_width=2000
        print("prepare screen size - set up")

@pytest.fixture(scope="function")
def open_browser_google(chose_size_of_screen):
        browser.open('https://www.google.ru/?hl=ru')
        print("this is beginning of fixture - set up")
        yield
        browser.quit()
        print("end of fixture - tear down")

