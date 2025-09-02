from bank import value

# python -m pytest test_bank.py


def test_0():
    assert value("hello") == 0


def test_20():
    assert value("hey") == 20


def test_100():
    assert value("oh") == 100


def test_case_sensitvity():
    assert value("HELLO!!") == 0
