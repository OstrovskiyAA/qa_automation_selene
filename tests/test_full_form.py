import pytest
from selene import browser, be, have, query, by
from selene.core.command import js, select_all, __select_all_actions
import os
from selenium import webdriver

import tests


def test_student_registrate(open_browser):
    browser.open("/automation-practice-form")
    browser.element("[id=firstName]").should(be.blank).type("Alexey")

    browser.element("#lastName").should(be.blank).perform(
        command=js.set_value("Ostrovskiy")
    )

    browser.element("[id=userEmail]").should(be.blank).type("a.a.ostrovskiy@mail.ru")

    # male = browser.element('[id="gender-radio-1"]').should(be.present)
    # male.perform(command=js.click)
    browser.all("[name=gender]").element_by(have.value("Male")).element("..").click()
    # browser.element("[name=gender][value=Male]").click()

    # with_ - используется для разовой настройки
    browser.all("[id^=userNumb]")[2].should(be.blank).with_(
        set_value_by_js=True
    ).set_value("8911277596")

    browser.element('[id="dateOfBirthInput"]').should(be.visible).click()
    # ^ - начинается с, ~ - то что такое точно есть в тексте с классом точка означает тоже самое
    browser.element("[class~=react-datepicker__month-select]").all("option")[4].click()
    browser.element("[class~=react-datepicker__year-select]").send_keys("1992")
    browser.all(f".react-datepicker__day--0{30}")[1].click()
    # browser.element('[id="dateOfBirthInput"]').should(be.visible).perform(command=select_all).type('30 May 1992').press_enter()

    browser.element("#subjectsInput").type("Computer Science").press_enter()

    # reading = browser.element('[id="hobbies-checkbox-2"]').should(be.present)
    # reading.perform(command=js.click)
    browser.all(".custom-checkbox").element_by(have.text("Music")).click()

    browser.element('[id="currentAddress"]').should(be.blank).type("Дачный проспект")

    browser.element("#state").perform(command=js.scroll_into_view).click()
    browser.all("[id^=react-select][id*=option]").element_by(
        have.exact_text("NCR")
    ).click()

    browser.element(".css-1wa3eu0-placeholder").should(be.present).should(
        have.text("Select City")
    ).click()
    browser.all("[id^=react-select][id*=option]").element_by(
        have.exact_text("Gurgaon")
    ).click()
    browser.element("#uploadPicture").set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(tests.__file__), "resources/me.jpg")
        )
    )
    browser.element('[id = "submit"]').should(be.present).perform(command=js.click)

    browser.element(".table").all("td").even.should(
        have.exact_texts(
            "Alexey Ostrovskiy",
            "a.a.ostrovskiy@mail.ru",
            "Male",
            "8911277596",
            "30 May,1992",
            "Computer Science",
            "Music",
            "me.jpg",
            "Дачный проспект",
            "NCR Gurgaon",
        )
    )
