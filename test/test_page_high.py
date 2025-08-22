import time

import allure
from selene import browser

from for_high_level.validate_form import FormValidator
from for_high_level.open_html_path_high import PhotoPage, BrowserPage, RegistrationPage, FormPage
from for_high_level.user import User


@allure.feature('Taste Case : Заполнение формы регистрации')
def test_requirement_form():
    open_machin = FormPage()
    photo_for_import = PhotoPage()
    personal_data = BrowserPage()
    get_send = RegistrationPage()
    user = User()
    form = FormValidator()
    open_machin.open()
    open_machin.delete_ad()

    allure.dynamic.title(f"Регистрация студента {user.full_name}")

    with allure.step('Заполнение фамилии и имени'):
        # заполнение личных данных
        personal_data.students_registration_first_name(user.first_name)
        personal_data.students_registration_last_name(user.last_name)

    with allure.step('Заполнение электронной почты'):
        # заполнение эл почты
        personal_data.students_registration_mail(user.mail)

    with allure.step('Выбор чекбокса пола'):
        # выбор чекбокса Female
        personal_data.students_registration_gender(user.gender)

    with allure.step('Ввод номера телефона'):
        # ввод номера телефона
        personal_data.students_registration_phone(user.phone)

    with allure.step('Ввод даты'):
        # ввод даты
        personal_data.students_registration_date_of_birth(user.year,user.moth,user.day)

    with allure.step('Заполнение subject'):
        # заполнение области subject
        personal_data.students_registration_subject(user.sub)

    with allure.step('Выбор чекбокса Hobbies'):
        # выбор чекбокса Hobbies
        personal_data.students_registration_checkbox(user.hobbies)

    with allure.step('Загрузка файла'):
        # загрузка файла
        personal_data.students_registration_photo(photo_for_import.import_file(user.picture))

    with allure.step('Заполнение Current Address'):
        # заполнение Current Address
        personal_data.students_registration_address(user.address)

    with allure.step('Выбор штата'):
        # выбор штата
        personal_data.students_registration_state()

    with allure.step('Выбор города'):
        # выбор города
        personal_data.students_registration_city()

    with allure.step('Отправка формы'):
        # вызов submit
        get_send.press_submit()

    with allure.step('Проверка формы'):
        # проверка формы
        form.validate_form(user)
