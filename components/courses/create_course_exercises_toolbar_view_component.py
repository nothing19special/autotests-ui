from playwright.sync_api import Page, expect
from components.base_component import BaseComponent

class CreateCourseExercisesToolbarViewComponent (BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

