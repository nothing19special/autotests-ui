from elements.button import Button
from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        #Локаторы страницы регистрации
        self.registration_form = RegistrationFormComponent(page)

        self.registration_button_click = Button(page, 'registration-page-registration-button', 'Registration Button')

    #Метод для завершения регистрации. Нажатие на кнопку
    def click_registration_button(self):
        self.registration_button_click.click()



