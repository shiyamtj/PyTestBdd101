import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities.locatorbuilder import LocatorBuilder
from utilities.logger import Logger

log = Logger(__name__, logging.INFO)
locator_builder = LocatorBuilder()

class BasePage:

    def __init__(self, driver, wait_time):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, wait_time)

    def click(self, locator_string):
        by_tuple = locator_builder.get_element_locator(locator_string)
        self._wait_and_find_element(by_tuple).click()
        log.logger.info(f"[Click] On element {locator_string}")

    def type(self, locator_string, value):
        by_tuple = locator_builder.get_element_locator(locator_string)
        self._wait_and_find_element(by_tuple).send_keys(value)
        log.logger.info(f"[Type] On element {locator_string} typing as {value}")

    def get_text(self, locator_string):
        by_tuple = locator_builder.get_element_locator(locator_string)
        text = self._wait_and_find_element(by_tuple).text
        log.logger.info(f"[Get Text] On element {locator_string}")
        return text

    def is_visible(self, locator_string, wait=10):
        short_wait = WebDriverWait(self.driver, int(wait))
        by_tuple = locator_builder.get_element_locator(locator_string)
        try:
            return_value = short_wait.until(EC.visibility_of_element_located(by_tuple)).is_displayed()

        except Exception as e:
            print(e)
            return_value = False
            log.logger.info(f"[Exception] On element {locator_string} with exception message as {e}")

        log.logger.info(f"[Wait for visible] On element {locator_string}")
        return return_value

    def _wait_and_find_element(self, locator_string):
        by = locator_builder.get_element_locator(locator_string)
        return self.wait.until(EC.presence_of_element_located(by))

    def _wait_and_find_elements(self, locator_string):
        by = locator_builder.get_element_locator(locator_string)
        return self.wait.until(EC.presence_of_element_located(by))
