import pytest

from theseus_growth import curve_functions


@pytest.fixture
def example_fixture_x():
    x = 3

    return x


def test_log_func():
    a = -15
    b = 3
    c = 20
    x = 3

    assert curve_functions.log_func(x, a, b, c) == 58.77443751081734


def test_log_func_fixture_example(example_fixture_x):
    a = -15
    b = 3
    c = 20

    assert curve_functions.log_func(example_fixture_x, a, b, c) == 58.77443751081734
