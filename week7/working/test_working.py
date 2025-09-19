import pytest
from working import convert
# python -m pytest test_working.py

def test_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:45 AM") == "22:30 to 08:45"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("1:15 PM to 3:45 PM") == "13:15 to 15:45"    
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"

def test_invalid_time():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")  # Invalid format
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")  # Invalid hour
    with pytest.raises(ValueError):
        convert("10:61 AM to 5 PM")  # Invalid minute
    with pytest.raises(ValueError):
        convert("10 AM to 5 XM")  # Invalid period
    with pytest.raises(ValueError):
        convert("10AM to 5PM")  # Missing spaces
