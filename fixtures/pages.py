import pytest
from playwright.sync_api import Page

from fixtures.browsers import chromium_page
from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage

@pytest.fixture
def registration_page(chromium_page: Page):
    return RegistrationPage(page=chromium_page)

@pytest.fixture
def dashboard_page(chromium_page: Page):
    return DashboardPage(page=chromium_page)