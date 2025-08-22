from selene import have, browser

class FormValidator:
    @staticmethod
    def validate_form(user):
        """Проверяет форму по данным пользователя, не изменяя старый код"""
        browser.all('.table-responsive td:nth-child(2)').should(have.texts(
            user.full_name,
            user.mail,
            user.gender,
            user.phone,
            user.birth_day,
            user.sub,
            user.hobbies,
            user.picture,
            user.address,
            user.region
        ))