from pages.base_page import BasePage
from pages.locators import Locators

class SauceDemoLoginPage(BasePage):
    URL = 'https://www.saucedemo.com/'

    def __init__(self, driver, wait_time):
        super().__init__(driver, wait_time)

    def load(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.type(Locators.locator_login_username, username)
        self.type(Locators.locator_login_password, password)
        self.click(Locators.locator_login_submit)