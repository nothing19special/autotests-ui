import pytest
from playwright.sync_api import Page
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.registration
@pytest.mark.regression
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill('mail@test.test', 'password', 'nickname')
    registration_page.registration_form.check_visible('mail@test.test', 'password', 'nickname')
    registration_page.click_registration_button()
    dashboard_page.check_visible_dashboard_title()

