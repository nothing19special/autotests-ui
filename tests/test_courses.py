from playwright.sync_api import sync_playwright, expect, Page
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    # Прямой переход на страницу "Courses"
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    # Проверка заголовка
    course_title_check = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(course_title_check).to_be_visible()
    expect(course_title_check).to_have_text('Courses')

    # Проверка результатов
    course_empty_results_check = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(course_empty_results_check).to_be_visible()
    expect(course_empty_results_check).to_have_text('There is no results')

    # Проверка иконки
    course_empty_icon_check = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(course_empty_icon_check).to_be_visible()

    # Проверка описания
    course_empty_description_check = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(course_empty_description_check).to_be_visible()
    expect(course_empty_description_check).to_have_text('Results from the load test pipeline will be displayed here')


