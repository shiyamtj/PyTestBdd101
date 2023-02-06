from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class DuckDuckGoPage:
    URL = 'https://www.duckduckgo.com'

    # locators
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input_element = self.browser.find_element(*self.SEARCH_INPUT)
        search_input_element.send_keys(phrase + Keys.RETURN)
