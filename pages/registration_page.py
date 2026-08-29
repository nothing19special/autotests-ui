from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        #Локаторы страницы регистрации
        self.registration_email_form = page.get_by_test_id('registration-form-email-input').locator('input')
        self.registration_username_form = page.get_by_test_id('registration-form-username-input').locator('input')
        self.registration_password_form = page.get_by_test_id('registration-form-password-input').locator('input')
        self.registration_button_click = page.get_by_test_id('registration-page-registration-button')

    #Метод для заполнения формы регистрации
    def  fill_registration_form(self, email, username, password):
        self.registration_email_form.fill(email)
        expect(self.registration_email_form).to_have_value(email)

        self.registration_username_form.fill(username)
        expect(self.registration_username_form).to_have_value(username)

        self.registration_password_form.fill(password)
        expect(self.registration_password_form).to_have_value(password)

    #Метод для завершения регистрации. Нажатие на кнопку
    def click_registration_button(self):
        self.registration_button_click.click()



