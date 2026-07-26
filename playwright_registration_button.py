from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    #Переход на страницу регистрации
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    #Проверка состояния кнопки до ввода данных
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    #Ввод почты (с использованием type (решил попробовать в этом тесте))
    registration_email_form = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_form.focus()
    for char in 'user.name@gmail.com':
        page.keyboard.type(char)

    #Ввод логина
    registration_username_form = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_form.focus()
    for char in 'username':
        page.keyboard.type(char)

    #Ввод пароля
    registration_password_form = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_form.focus()
    for char in 'password':
        page.keyboard.type(char)

    #Проверка состояния кнопки после ввода данных
    expect(registration_button).to_be_enabled()

