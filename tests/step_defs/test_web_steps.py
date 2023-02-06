from pytest_bdd import scenarios, given, when, then, parsers
from pages.Pages import Pages

# Scenarios
scenarios('../features/saucedemoweb.feature')


@given('the SauceDemo login page is displayed', target_fixture='web_browser')
def web_browser(browser, config_wait_time, request):
    pages = Pages(browser, config_wait_time)  # initializing all pages
    request.pages = pages  # shared variable
    request.pages.SauceDemoLoginPage.load()


@when(parsers.parse('the user login with username as "{username}" and password as "{password}"'))
def user_login_with_credentials(request, username, password):
    request.pages.SauceDemoLoginPage.login(username, password)


@then(parsers.parse('the user should able to see dashboard loaded'))
def user_on_dashboard(request):
    is_loaded = request.pages.SauceDemoDashboardPage.is_loaded()
    assert is_loaded == True, 'Dashboard not loaded'
