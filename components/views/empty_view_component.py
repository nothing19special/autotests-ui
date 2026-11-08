from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page,f'{identifier}-empty-view-icon', 'Icon')
        self.title = Text(page,f'{identifier}-empty-view-title-text', 'Title')
        self.description = Text(page,f'{identifier}-empty-view-description-text', 'Description')

    def check_visible(self, title: str, description: str):
        # Проверяем видимость иконки
        expect(self.icon).to_be_visible()

        # Проверяем видимость заголовка и его текст
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)

        # Проверяем видимость описания и его текст
        expect(self.description).to_be_visible()
        expect(self.description).to_have_text(description)