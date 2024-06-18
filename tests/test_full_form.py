import pytest
from selene import browser, be, have, query, by
from selene.core.command import js, select_all, __select_all_actions
import os
from selenium import webdriver
import json

import allure
from allure import attachment_type
import tests
from pages.registration_page import RegistrationPage
from allure_commons.types import Severity

registration_page = RegistrationPage()


@allure.label("owner", "Ostrovskiy Alexey")
@allure.severity(Severity.CRITICAL)
@allure.story("Checking registration")
@allure.feature("new tasks")
@allure.link("https://demoqa.com", name="Testing")
def test_student_registrate(open_browser):
    registration_page.open()
    registration_page.fill_first_name()
    registration_page.fill_last_name()
    registration_page.fill_email()
    registration_page.select_gender()
    registration_page.fill_mobile_number()
    # registration_page.fill_date()
    registration_page.fill_date_by_your_own(30, "May", 1992)
    registration_page.fill_subject()
    registration_page.fill_hobby()
    registration_page.dowload_file()
    registration_page.fill_address()
    registration_page.fill_state()
    registration_page.fill_city()
    registration_page.submit()
    registration_page.should_have_registered(
        "Alexey",
        "Ostrovskiy",
        "a.a.ostrovskiy@mail.ru",
        "Male",
        "8911277596",
        "30 May,1992",
        "Computer Science",
        "Music",
        "me.jpg",
        "Дачный проспект",
        "NCR",
        "Gurgaon",
    )
