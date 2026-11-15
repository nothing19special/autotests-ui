from typing import Self

from playwright.sync_api import Page, expect

from components import dashboard
from components.base_component import BaseComponent
from elements.text import Text
from playwright_registration import dashboard_title_check


class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page ):
        super().__init__(page)

        self.dashboard_title = Text(page,'dashboard-toolbar-title-text','Dashboard Toolbar Title')

    def check_visible(self):
        self.dashboard_title.check_visible()
        self.dashboard_title.check_have_text('Dashboard')