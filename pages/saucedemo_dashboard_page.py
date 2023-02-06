from pages.base_page import BasePage
from pages.locators import Locators

class SauceDemoDashboardPage(BasePage):
    def __init__(self, driver, wait_time):
        super().__init__(driver, wait_time)

    def is_loaded(self):
        return self.is_visible(Locators.locator_dashboard_inventory_container)