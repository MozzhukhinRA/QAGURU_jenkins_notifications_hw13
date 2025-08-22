import os
import time

from selene import be, browser, have

class FormPage:
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        time.sleep(10)
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
        return self

class PhotoPage:

    def import_file(self, photo):
        import_file = os.path.join(os.path.dirname(__file__), photo)
        return import_file


class BrowserPage:

    def students_registration_first_name(self, value):
        browser.element('#firstName').should(be.visible).type(value)


    def students_registration_last_name(self, value):
        browser.element('#lastName').should(be.visible).type(value)


    def students_registration_mail(self, value):
        browser.element('#userEmail').should(be.visible).type(value)


    def students_registration_gender(self, gender):
        browser.all('.custom-control-input').element_by(have.value(gender)).element('..').click()


    def students_registration_phone(self, value):
        browser.element('#userNumber').should(be.visible).type(value)


    def students_registration_date_of_birth(self, year, moth, day):
        browser.element('#dateOfBirthInput').should(be.visible).click()
        browser.element('.react-datepicker__month-select').type(moth)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}').click()
        return f'{day} {moth},{year}'

    def students_registration_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def students_registration_checkbox(self, value):
        browser.all('.custom-control').element_by(have.exact_text(value)).click()

    def students_registration_photo(self, values : PhotoPage):
        browser.element('.form-control-file').with_(timeout=5).should(be.visible).send_keys(values)

    def students_registration_address(self, value):
        browser.element('#currentAddress').should(be.visible).type(value)

    def students_registration_state(self):
        browser.element('#state').click()
        browser.element('#react-select-3-option-1').click()

    def students_registration_city(self):
        browser.element('#city').click()
        browser.element('#react-select-4-option-2').click()

class RegistrationPage:

    def press_submit(self):
        browser.element('#submit').press_enter()

    def assert_form(self, full_name, mail, gender, phone, birth_day, sub, hobbies, picture, address, region):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        browser.all('.table-responsive td:nth-child(2)').should(have.texts(
            full_name,
            mail,
            gender,
            phone,
            birth_day,
            sub,
            hobbies,
            picture,
            address,
            region
        ))
