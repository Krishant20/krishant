import pytest


def test_creditcard():
    print("Creditcard")


@pytest.mark.smoke
@pytest.mark.skip
def test_creditcard3():
    print("Creditcard2")


@pytest.fixture()
def setup():
    print("I will be executing first")
    yield
    print("Completed")


def test_demofixture(setup):
    print("executing now")

def test_crossBrowser(CrossBrowser):
    print("CrossBrowser[1]")