import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("Completed")


@pytest.fixture()
def DataLoad():
    print("user profile data being created")
    return ["Rahul", "Krishant", "krishant1589@gmail.com"]


@pytest.fixture(params=[("chrome", "Rahul", "krishant"), ("Firefox", "jeevan", "Bhai"), ("IE", "Ram", "Siyaram")])
def CrossBrowser(request):
    return request.param
