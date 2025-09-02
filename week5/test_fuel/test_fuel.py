import pytest
import fuel


def test_fraction():
    assert fuel.convert("3", "4") == 75
    assert fuel.convert("1", "2") == 50


def test_gauge():
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(100) == "F"
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(49) == "49%"


def test_exceptions():
    # non-integer input
    with pytest.raises(ValueError):
        fuel.convert("a", "b")
    with pytest.raises(ValueError):
        fuel.convert("three", "four")

    # denominator zero
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1", "0")

    # numerator > denominator
    with pytest.raises(ValueError):
        fuel.convert("5", "2")

    # negative values
    with pytest.raises(ValueError):
        fuel.convert("-1", "2")
    with pytest.raises(ValueError):
        fuel.convert("1", "-2")
