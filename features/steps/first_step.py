from pytest_bdd import given, when, then
from main import solution

@given('')
def given_impl(context):
# It is out of order.
    pass

@when('')
def when_impl(context):
    assert (solution("") == [])

@then('')
def then_impl(context):
	assert (solution("") == [])