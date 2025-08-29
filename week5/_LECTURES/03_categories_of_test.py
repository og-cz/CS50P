from calculator import square
import pytest 
# pytest 03_categories_of_test.py


def test_postive():
    assert square(2) == 4
    assert square(3) == 6  # only this will fail


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_str():
    with pytest.raises(TypeError):
        square("cat")

