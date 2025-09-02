from twttr import shorten

# python -m pytest test_twttr.py


def test_lower_words():
    assert shorten("banana") == "bnn"
    assert shorten("mango") == "mng"
    assert shorten("singapore") == "sngpr"


def test_upper_words():
    assert shorten("SINGAPORE") == "SNGPR"
    assert shorten("BANANA") == "BNN"
    assert shorten("MANGO") == "MNG"


def test_numbers():
    assert shorten("HAHA123") == "HH123"
    assert shorten("15125412") == "15125412"


def test_error():
    assert shorten("...twitter") == "...twttr"
