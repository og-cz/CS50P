from plates import is_valid

# 1. “All vanity plates must start with at least two letters.”
# 2. “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# 3. “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# 4. “No periods, spaces, or punctuation marks are allowed.”

# python -m pytest test_plates.py


def test_is_valid_1():
    assert is_valid("A") == False
    assert is_valid("AB") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("XXXX") == True


def test_is_valid_2():
    assert is_valid("A12313") == False
    assert is_valid("ABDE22") == True
    assert is_valid("123ABC") == False
    assert is_valid("XXXX20") == True


def test_is_valid_3():
    assert is_valid("ABC1DE") == False
    assert is_valid("ABC123") == True


def test_is_valid_4():
    assert is_valid("ABC123") == True
    assert is_valid("AB0123") == False


def test_is_valid_5():
    assert is_valid("AB/#'!") == False
    assert is_valid("AB2B..") == False
    assert is_valid("ABC123#!") == False
    assert is_valid("!DWEQ2") == False
    assert is_valid("      ") == False
