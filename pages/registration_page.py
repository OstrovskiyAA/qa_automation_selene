import os

from selene import browser, be, have
from selene.core.command import js, select_all
import allure
import tests


class RegistrationPage:
    def __init__(self):
        pass

    def open(self):
        browser.open("/automation-practice-form")

    @allure.step("Insert first name")
    def fill_first_name(self, first_name="Alexey"):
        browser.element("[id=firstName]").should(be.blank).type(first_name)

    @allure.step("Insert last name")
    def fill_last_name(self, last_name="Ostrovskiy"):
        browser.element("#lastName").should(be.blank).perform(
            command=js.set_value(last_name)
        )

    @allure.step("Insert email")
    def fill_email(self, email="a.a.ostrovskiy@mail.ru"):
        browser.element("[id=userEmail]").should(be.blank).type(email)

    @allure.step("Insert gender")
    def select_gender(self, gender="Male"):
        browser.all("[name=gender]").element_by(have.value(gender)).element(
            ".."
        ).click()
        # male = browser.element('[id="gender-radio-1"]').should(be.present)
        # male.perform(command=js.click)
        # browser.element("[name=gender][value=Male]").click()

    @allure.step("Insert mobile number")
    def fill_mobile_number(self, phone_nimber="8911277596"):
        browser.all("[id^=userNumb]")[2].should(be.blank).with_(
            set_value_by_js=True
        ).set_value(phone_nimber)

    @allure.step("Insert date of birth")
    def fill_date(self, day=30, month=5, year=1992):
        browser.element('[id="dateOfBirthInput"]').should(be.visible).click()
        # ^ - начинается с, ~ - то что такое точно есть в тексте с классом точка означает тоже самое
        browser.element("[class~=react-datepicker__month-select]").all("option")[
            month - 1
        ].click()
        browser.element("[class~=react-datepicker__year-select]").send_keys(year)
        browser.all(f".react-datepicker__day--0{day}")[1].click()
        # with_ - используется для разовой настройки

    @allure.step("Insert date of birth")
    def fill_date_by_your_own(self, day=30, month="May", year=1992):
        browser.element('[id="dateOfBirthInput"]').should(be.visible).perform(
            command=select_all
        ).type(f"{day} {month} {year}").press_enter()

    @allure.step("Insert subject")
    def fill_subject(self, subject="Computer Science"):
        browser.element("#subjectsInput").type(subject).press_enter()

    @allure.step("Insert hobby")
    def fill_hobby(self):
        browser.all(".custom-checkbox").element_by(have.text("Music")).click()

    @allure.step("Download file")
    # reading = browser.element('[id="hobbies-checkbox-2"]').should(be.present)
    # reading.perform(command=js.click)
    def dowload_file(self):
        browser.element("#uploadPicture").set_value(
            os.path.abspath(
                os.path.join(os.path.dirname(tests.__file__), "resources/me.jpg")
            )
        )

    @allure.step("Insert address")
    def fill_address(self, address="Дачный проспект"):
        browser.element('[id="currentAddress"]').should(be.blank).type(address)

    @allure.step("Insert state")
    def fill_state(self, state="NCR"):
        browser.element("#state").perform(command=js.scroll_into_view).click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(state)
        ).click()

    @allure.step("Insert city")
    def fill_city(self, city="Gurgaon"):
        browser.element(".css-1wa3eu0-placeholder").should(be.present).should(
            have.text("Select City")
        ).click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(city)
        ).click()

    def submit(self):
        browser.element('[id = "submit"]').should(be.present).perform(command=js.click)

    def should_have_registered(
        self,
        first_name,
        last_name,
        email,
        gender,
        mobile_phone,
        date_of_birth,
        subject,
        hobby,
        image,
        address,
        state,
        city,
    ):
        browser.element(".table").all("td").even.should(
            have.exact_texts(
                f"{first_name} {last_name}",
                email,
                gender,
                mobile_phone,
                date_of_birth,
                subject,
                hobby,
                image,
                address,
                f"{state} {city}",
            )
        )
