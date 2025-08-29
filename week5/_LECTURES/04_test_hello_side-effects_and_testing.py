from hello import hello  # import funciton hello from hello.py


# pytest 04_test_hello_side-effects_and_testing.py
def test_default():
    assert (
        hello("david") == "hello, david"
    )  # this error beacuse initially its not returnign the value on hello.py so it has nothing to compare
    assert hello() == "hello, x"


def tests_argument():
    for name in ["hermione", "harry", "ron"]:
        assert hello(name) == f"hello, {name}"
