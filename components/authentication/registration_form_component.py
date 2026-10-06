from playwright.sync_api import Page, expect

from components.base_component import BaseComponent

class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_form = page.get_by_test_id('registration-form-email-input').locator('input')
        self.username_form = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_form = page.get_by_test_id('registration-form-password-input').locator('input')

    def fill(self, email, username, password):
        self.email_form.fill(email)
        self.username_form.fill(username)
        self.password_form.fill(password)

    def check_visible(self, email: str, username: str, password: str):
        expect(self.email_form).to_have_value(email)
        expect(self.username_form).to_have_value(username)
        expect(self.password_form).to_have_value(password)

