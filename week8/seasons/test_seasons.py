import pytest
from datetime import date, timedelta
from seasons import BirthDate, get_date, get_minutes_lived, convert_into_words

    # python -m pytest test_seasons.py

def test_valid_birthdate():
    today = date.today()
    ten_days_ago = today - timedelta(days=10)
    b = BirthDate(ten_days_ago.strftime("%Y-%m-%d"))
    assert b.birthdate == ten_days_ago

def test_minutes_lived():
    today = date.today()
    two_days_ago = today - timedelta(days=2)
    b = BirthDate(two_days_ago.strftime("%Y-%m-%d"))
    assert b.minutes_lived() == 2 * 24 * 60

def test_invalid_month():
    with pytest.raises(SystemExit):
        BirthDate("2020-13-01")

def test_invalid_day():
    with pytest.raises(SystemExit):
        BirthDate("2020-12-32")

def test_invalid_format():
    with pytest.raises(SystemExit):
        BirthDate("2020/12/01")

def test_get_date():
    b = get_date("2020-01-01")
    assert isinstance(b, BirthDate)
    assert b.birthdate == date(2020, 1, 1)

def test_get_minutes_lived():
    today = date.today()
    one_day_ago = today - timedelta(days=1)
    b = BirthDate(one_day_ago.strftime("%Y-%m-%d"))
    assert get_minutes_lived(b) == 1 * 24 * 60

def test_convert_into_words():
    assert convert_into_words(1440) == "One thousand four hundred and forty minutes"

