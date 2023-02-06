from selenium.webdriver.common.by import By


class LocatorBuilder:
    def get_element_locator(self, locator):
        tuple_locator = tuple(locator)

        locator_strategy = tuple_locator[0].lower()
        locator_strategy_value = tuple_locator[1]
        if locator_strategy.__contains__("id"):
            return By.ID, locator_strategy_value

        elif locator_strategy.__contains__("xpath"):
            return By.XPATH, locator_strategy_value

        elif locator_strategy.__contains__("class_name"):
            return By.CLASS_NAME, locator_strategy_value

        elif locator_strategy.__contains__("css_selector"):
            return By.CSS_SELECTOR, locator_strategy_value

        elif locator_strategy.__contains__("name"):
            return By.NAME, locator_strategy_value

        elif locator_strategy.__contains__("link_text"):
            return By.LINK_TEXT, locator_strategy_value

        elif locator_strategy.__contains__("partial_link_text"):
            return By.PARTIAL_LINK_TEXT, locator_strategy_value

        else:
            raise NotImplementedError(f'[Critical] Undefined locator strategy "{locator_strategy}"')
