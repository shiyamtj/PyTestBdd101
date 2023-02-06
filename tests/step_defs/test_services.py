import requests
from pytest_bdd import scenarios, given, then, parsers

from tests.step_defs.conftest import DUCKDUCKGO_API

# scenarios
scenarios('../features/duckduckgoservices.feature')

@given(parsers.parse('the DuckDuckGo API is queries with "{phrase}"'), target_fixture='api_response')
def api_response(phrase):
    params = {'q': phrase, 'format': 'json'}
    response = requests.get(DUCKDUCKGO_API, params=params)
    return response


@then(parsers.cfparse('the response contains results for "{phrase}"'))
def api_response_contents(api_response, phrase):
    assert phrase.lower() == api_response.json()['Heading'].lower()


@then(parsers.parse('the response status code is "{code:d}"'))
def api_response_code(api_response, code):
    assert api_response.status_code == code
