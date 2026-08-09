from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list():
    with sync_playwright() as playwright:
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

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        # Прямой переход на страницу "Courses"
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        # Проверка заголовка
        course_title_check = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(course_title_check).to_be_visible()
        expect(course_title_check).to_have_text('Courses')

        # Проверка результатов
        course_empty_results_check = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(course_empty_results_check).to_be_visible()
        expect(course_empty_results_check).to_have_text('There is no results')

        # Проверка иконки
        course_empty_icon_check = page.get_by_test_id('courses-list-empty-view-icon')
        expect(course_empty_icon_check).to_be_visible()

        # Проверка описания
        course_empty_description_check = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(course_empty_description_check).to_be_visible()
        expect(course_empty_description_check).to_have_text(
            'Results from the load test pipeline will be displayed here')


