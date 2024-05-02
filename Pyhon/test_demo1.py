import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")

def test_ScondProgram(setup):
    msg = "Hello"
    assert msg == "Hello"
    assert msg == "Hi"


def test_creditcard2():
    print("Creditcard2")