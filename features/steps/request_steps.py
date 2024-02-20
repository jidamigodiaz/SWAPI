import requests
from behave import *
from features.utilities import utils


@given('I get from "{url}" with suffix "{parameter}"')
def step_impl(context, url, parameter):
    context.response = requests.get(url + parameter)


@then('I should see a response code "{response}"')
def step_impl(context, response):
    assert context.response.status_code == int(response)


@then('I should see an "{field}" in each "{response_field}" of response')
def step_impl(context, field, response_field):
    results = context.response.json()[response_field]
    for element in results:
        assert field in element, f"fields is not present in some element: {element}"


@then('I should see a "{field_name}" string field in each "{response_field}" of response starting with "{prefix}"')
def step_impl(context, field_name, response_field, prefix):
    results = context.response.json()[response_field]
    for element in results:
        assert element[field_name].startswith(prefix), f"some fields doesn't start with {prefix}: {element[field_name]}"


@then('I should see "{string_of_elements}" list in the body response')
def step_impl(context, string_of_elements):
    body = context.response.json()
    list_of_elements = [i.strip() for i in list(string_of_elements.split(","))]
    for e in list_of_elements:
        assert e in body, f"some element is not found, list of elements: '{list_of_elements}', body: {body}"


@then('I should see a list of fields named "{string_of_elements}" starting with "{prefix}" in body response')
def step_impl(context, string_of_elements, prefix):
    body = context.response.json()
    list_of_elements = [i.strip() for i in list(string_of_elements.split(","))]
    for e in list_of_elements:
        assert body[e].startswith(prefix), f"some fields doesn't start with {prefix}: {body[e]}"


@then('I should see one "{response_field}" with name "{name}"')
def step_impl(context, response_field, name):
    results = context.response.json()[response_field]
    assert len(utils.search_in_list('name', name, results)) == 1


@when('I get details from element with name "{name}" in "{response_field}" of response')
def step_imp(context, name, response_field):
    results = context.response.json()[response_field]
    element = utils.search_in_list('name', name, results)
    context.response = requests.get(element[0]['url'])
