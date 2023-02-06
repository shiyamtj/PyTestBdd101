from pages.saucedemo_dashboard_page import SauceDemoDashboardPage
from pages.saucedemo_login_page import SauceDemoLoginPage

class Pages:
    def __init__(self, driver, wait_time):
        self.SauceDemoLoginPage = SauceDemoLoginPage(driver, wait_time)
        self.SauceDemoDashboardPage = SauceDemoDashboardPage(driver, wait_time)