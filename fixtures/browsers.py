import pytest
from playwright.sync_api import sync_playwright, Page, Playwright


#Открытие страницы. Без дополнительных параметров
@pytest.fixture(scope='session')
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()


#Создание пользака для получения данных авторизации
@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Переход на страницу регистрации
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Ввод почты
    registration_email_form = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_form.fill('email@test.test')

    # Ввод никнейма
    registration_username_form = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_form.fill('username')

    # Ввод пароля
    registration_password_form = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_form.fill('password')

    # Нажатия на кнопку регистрации
    registration_button_click = page.get_by_test_id('registration-page-registration-button')
    registration_button_click.click()

    # Сохранения состояния клиента
    context.storage_state(path='browser-state.json')


#Создание страницы с новым контекстом
@pytest.fixture(scope='function')
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    #Возвращение страницы
    yield page
    #Закрытие браузера (опционально)
    browser.close()




