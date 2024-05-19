import pytest
from selene import browser, be, have, query
from selene.core.command import js


def test_student_registrate(open_browser):
    browser.open('/automation-practice-form')
    browser.element('[id="firstName"]').should(be.blank).type('Alexey')
    browser.element('[id="lastName"]').should(be.blank).type('Ostrovskiy')
    browser.element('[id="userEmail"]').should(be.blank).type('a.a.ostrovskiy@mail.ru')
    browser.element('[id="gender-radio-1"]').perform(command=js.click)
    browser.element('[id="userNumber"]').should(be.blank).type('89112775960')
    browser.element('[id="dateOfBirthInput"]').perform(command=js.click)