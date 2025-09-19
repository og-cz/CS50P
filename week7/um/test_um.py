import pytest
from um import count
import sys
# python -m pytest test_um.py


def test():
    assert count('um') == 1
    assert count('um yea um') == 2
    assert count('umm') == 0
    assert count('oh yea yummy') == 0
    assert count('Um') == 1
    assert count('UM uM umm') == 2
