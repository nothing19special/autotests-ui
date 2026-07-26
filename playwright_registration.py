from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False)
    page=browser.new_page()
    #Переход на страницу
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    #Ввод почты
    registration_email = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email.fill('user.name@gmail.com')

    #Ввод никнейма
    registration_username = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username.fill('username')

    #Ввод пароля
    registration_password = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password.fill('password')

    #Переход на страницу с дашбордами
    registration_button_click = page.get_by_test_id('registration-page-registration-button')
    registration_button_click.click()

    #Проверка наличия дашборда
    dashboard_title_check = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title_check).to_be_visible()
    expect(dashboard_title_check).to_have_text('Dashboard')



