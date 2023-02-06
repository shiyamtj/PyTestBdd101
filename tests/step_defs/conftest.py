
from pytest_bdd import given
from selenium.webdriver import Chrome, Firefox
from pathlib import Path
from py.xml import html
import pytest
import json

from pages.duckduckgo_page import DuckDuckGoPage

CONFIG_PATH = '../config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox']

# shared variable
DUCKDUCKGO_API = 'https://api.duckduckgo.com'


@pytest.fixture(scope='session')
def config():
    # Read the JSON config file and returns it as a parsed dict
    absolute_filepath = Path(__file__).parent / CONFIG_PATH
    with open(absolute_filepath) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def config_browser(config):
    # Validate and return the browser choice from the config data
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']


@pytest.fixture(scope='session')
def config_wait_time(config):
    # Validate and return the wait time from the config data
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture
def browser(config_browser, config_wait_time):
    # Initialize WebDriver
    if config_browser == 'chrome':
        driver = Chrome()
    elif config_browser == 'firefox':
        driver = Firefox()
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')
    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(config_wait_time)

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()


@given('the DuckDuckGo home page is displayed', target_fixture='web_browser')
def web_browser(browser):
    search_page = DuckDuckGoPage(browser)
    search_page.load()


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')


def pytest_html_report_title(report):
    report.title = "Report - PyTest 101"


def pytest_configure(config):
    config._metadata["Tester"] = "Shiyam Jannan"
    config._metadata["Environment"] = "QA"


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    session.config._metadata["Environment"] = "QA"
    session.config._metadata["Tester"] = "Shiyam Jannan"
    session.config._metadata["Status"] = exitstatus


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([html.p(
        """  As a gardener,
  I want to carry cucumbers in a basket,
  So that I don't drop them all""")])


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("http://www.example.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        report.extra = extra