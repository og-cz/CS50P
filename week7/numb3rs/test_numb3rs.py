import pytest
from numb3rs import validate

# python -m pytest test_numb3rs.py

def test_NUM():
    assert validate("255.255.255.255") == True
    assert validate('512.512.512.512') == False
    assert validate("1.2.3.1000") == False
    assert validate('192.168.001.1') == False
    assert validate('01.118.001.1') == False
    assert validate('121.0.0.1') == True

def test_STR():
    assert validate("cat") == False
    assert validate('0.0.1.wat') == False
    assert validate("dog.cat.dog.cat") == False
    assert validate('0000abc') == False