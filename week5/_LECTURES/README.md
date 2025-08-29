## unit test

- testing our own code with the code of our own?
- its a good common practice in making a project or in a real work tech to write a little extra code to test our own
  so writing our own test, so the problem that we are solving is working correctly.

  > or in short, its just saying testing individual unit of my code or program - so its typically functions

### assert

In Python, assert is used as a debugging aid.
It checks whether a condition is True.

- If the condition is True, nothing happens (the program continues).
- If the condition is False, it raises an AssertionError (and can optionally include an error message).

### assertion error

- An AssertionError is the specific type of error Python raises when an assert statement fails.
- assert 2 + 2 == 5

### pytest

pytest is a testing framework for Python.
It’s one of the most popular tools used by Python developers to write and run automated test

- What it does:

Lets you write tests as simple functions (no need for heavy setup).
Runs all your tests automatically.
Gives nice output showing what passed and what failed.
Works well with assert (you just use normal Python assert statements in tests).
Can generate reports, run only certain tests, or even run in parallel.

```terminal
============================================================ test session starts =============================================================
platform win32 -- Python 3.13.5, pytest-8.4.1, pluggy-1.6.0
rootdir: C:\Users\Asus\Documents\ogcz\_DEV\cs50p-journey\week5
collected 0 items / 1 error

=================================================================== ERRORS ===================================================================
_______________________________________________________ ERROR collecting 02_pytest.py ________________________________________________________
02_pytest.py:1: in <module>
    from calculator import square
calculator.py:13: in <module>
    main()
calculator.py:2: in main
    x = int(input("What's X? "))
            ^^^^^^^^^^^^^^^^^^^
C:\Users\Asus\AppData\Local\Programs\Python\Python313\Lib\site-packages\_pytest\capture.py:229: in read
    raise OSError(
E   OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.
-------------------------------------------------------------- Captured stdout ---------------------------------------------------------------
What's X?
========================================================== short test summary info ===========================================================
ERROR 02_pytest.py - OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
============================================================== 1 error in 0.14s ==============================================================
```

### side effects and testing

- its advice to not have a default paramter to avoid have side ffectes if we want to have our code testable

#### Pure Functions vs Functions with Side Effects

- Pure function: Only depends on input and returns output; no side effects.

```python
def square(x):
    return x * x
```

- Function with side effects: Changes something outside itself (variables, files, I/O, etc.).

```python
def add_to_list(lst, item):
    lst.append(item)  # modifies external list
```

### side effect of import issue (recall)

- In Python, any code that is not inside a function or class—and not guarded by:

```python
if __name__ == "__main__":
```

will run immediately when the file is imported, because Python executes the file top-to-bottom on import.

### collection of test

#### **init**.py Key Breakdown

- What it is
  A special Python file inside a folder.
  Can be empty or contain Python code.
  Marks the folder as a Python package.
  Runs automatically when the package is imported.

- Why use it
  Marks a folder as a package
  Without it, relative imports inside the folder can fail.
  Helps Python know that the folder is part of a package.
  Enables relative imports

  ```python
  # Inside tests/test_hello.py
  from .hello import hello   # requires __init__.py in tests/
  ```

  Organizational clarity
  Makes it clear that the folder contains related modules (like tests).
  Helps multiple programmers work together; everyone knows it’s a “package folder.”

### how to use?

```
week5/
├─ __init__.py         # marks week5 as a package
├─ hello.py            # your module
├─ 04_test_hello.py    # your pytest file
```

_two ways to import this_

```python
1:
    from folder_name.hello import hello
2 (reccomanded):
    from .hello import hello
# Requires __init__.py; without it, Python won’t recognize the folder as a package.
#  The . means “current package folder.” You can also do .. for parent package, etc
```
