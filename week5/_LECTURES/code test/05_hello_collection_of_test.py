from hello import hello  # import funciton hello from hello.py


# pytest 05_hello_collection_of_test.py
def test_default():
    assert hello("david") == "hello, david"
    assert hello() == "hello, x"


def tests_argument():
    for name in ["hermione", "harry", "ron"]:
        assert hello(name) == f"hello, {name}"
