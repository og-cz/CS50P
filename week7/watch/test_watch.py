import pytest
from watch import parse

# python -m pytest test_watch.py

def test():
    assert parse('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == 'https://www.youtube.com/xvFZjo5PgG0'
    assert parse('<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>') == 'https://www.youtube.com/xvFZjo5PgG0'
    assert parse('<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>') == None