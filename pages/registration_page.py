from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from components.authentication.registration_form_component import RegistrationFormComponent


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        #Локаторы страницы регистрации
        self.registration_form = RegistrationFormComponent(page)

        self.registration_button_click = page.get_by_test_id('registration-page-registration-button')

    #Метод для завершения регистрации. Нажатие на кнопку
    def click_registration_button(self):
        self.registration_button_click.click()



