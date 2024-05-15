from selene import browser, be, have
import pytest
from selenium import webdriver
#
# @pytest.fixture(scope='function', autouse=True)
# def browser_manager():
#     driver_options = webdriver.ChromeOptions()
#     driver_options.page_load_strategy = 'eager'
#     browser.config.driver_options = driver_options


def test_valid(open_browser):
    browser.element('[id="username"]').should(be.blank).type('a.a.ostrovskiy')
    browser.element('[id="password"]').should(be.blank).type('it').press_enter()
    browser.open('https://kpditmo.ru/course/view.php?id=23')
    browser.element('[class="h2"]').should(have.text('Введение в тестирование'))

def test_invalid(open_browser):
    browser.element('[id="username"]').should(be.blank).type('a.a.ostrovskiy')
    browser.element('[id="password"]').should(be.blank).type('0').press_enter()
    browser.element('[class="alert alert-danger"]').should(have.text('Неверный логин или пароль, попробуйте заново.'))

def test_search_in_google(open_browser_google):
    browser.element('[class="gLFyf"]').should(be.blank).type('итмо').press_enter()
    browser.element('[class="LC20lb MBeuO DKV0Md"]').should(have.text('Университет ИТМО'))