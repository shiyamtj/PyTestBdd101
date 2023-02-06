
from pytest_bdd import scenarios, given, when, then, parsers

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.duckduckgo_page import DuckDuckGoPage
from pages.duckduckgo_result_page import DuckDuckGoResultPage

# Scenarios
scenarios('../features/duckduckgoweb.feature')


@when(parsers.parse('the user searches for "{text}"'))
@when(parsers.parse('the user searches for the phrase:\n"""{text}"""'))
def search_phrase(browser, text):
    search_page = DuckDuckGoPage(browser)
    search_page.search(text)

@then(parsers.parse('one of the results contains "{phrase}"'))
def results_have_one(browser, phrase):
    result_page = DuckDuckGoResultPage(browser)
    assert result_page.link_div_count() > 0
    assert result_page.phrase_result_count(phrase) > 0

@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    result_page = DuckDuckGoResultPage(browser)
    result_page.search_input_value()

