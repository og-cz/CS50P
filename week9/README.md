# CS50p Week 9

- [Set](#set)
- [Global](#global)
- [Constants](#constants)
- [Type Hints](#type-hints)
  - [mypy](#mypy)
- [Docstrings](#docstrings)
- [Argparse](#argparse)
- [Unpacking](#unpacking)
  - [\*args](#3-args)
  - [\*\*kwargs](#4-kwargs)
- [Map Function](#map-function)
- [Passing a Function](#passing-a-function-difference)
- [List Comprehension](#list-comprehension)
- [Filter](#filter)
- [Dictionary Comprehensions](#dictionary-comprehensions)
- [Enumerate](#enumerate)
- [Generators](#generators)
  - [Yield](#yield)
  - [Iterators](#iterators)

### set

- in mathematics set is a collection of data where one`s data does not duplicate

  A set in Python is an unordered collection of unique, hashable elements. Use sets when you need uniqueness or fast membership tests (average O(1)). Sets are mutable (you can add/remove items); frozenset is the immutable variant.

### global

- we can initialize a variable on the top which is considered to a global variable
- we can read top variable but we cannot change it unless we implicitly say global balance

```python
balance = 0
global global_balance = 0
def main():
    print("balance:", balance)
    balance += n  # UnboundLocalError: cannot access local variable 'balance' where it is not associated with a value

def withdraw(n):
    global balance
    balance -= n # this would work because of global balance
```

### constants

- its basically just a unchangeble value in a variable
  BUT IN PYTHON, THERE IS NO WAY TO DO THIS SO THE BEST WAY TO DO THIS IN PYTHONIC WAY

```python
NUMBERS = 3
```

### type hints

- its just another way for python to know what data we are returning, it doesnt add logic but its just a remembrance like in constant that this is a int or string or whatever data
- its just specficiation which helps bug to be read easily

```python
number: int = 10
def meow(n: int): # this is a type hint, saying n must be a integer but not logically

def number_get() -> int: # this means the type hint for return
```

#### mypy

- is a program that understand type hint like a automatic try catch
  how to run

mypy module_name.py

### docstrings

- document strings
  how to have a documents in a function formally

```python
def func(n):
    """Bark n times."""
    return 'Bark\n' * n
```

proper format of documenting

```python
"""
    _type_: _description_
"""
```

### argparse

- it allows us to make our own command line type program using sys library
- python 07_argparse.py -n 3 > we can make our own meaning

how to use this?

1. import argparse and call the class ArgumentParser()
2. add_argument -> when you register a argument it expect a -text and matches a token
3. args = parser.parse_args() -> combine all the created args
4. then we can do "args.text" -> returns a value based form our command

```python
import argparse
parser = argparse.ArgumentParser(description="meow like a cat")
parser.add_argument("-n", help="number of times to print meow")
args = parser.parse_args()
```

### unpacking

Unpacking is assigning parts of an iterable (tuple/list/iterable) to multiple variables in one statement.

1. list unpacking

- star = [1,2,3]
- function(\*star) -> this passes every individual element from star

2. dictionary unpacking

- coins = {"a": 100, "b": 50, "c": 25}
- print(total(\*\*coins)) -> what this doing is returnign 3 values like a:100 is a=100
- like print(a=100, b=50, c=25)

3. \*args

- \*args collects any extra positional arguments into a tuple.

4. \*\*kwargs

- \*\*kwargs collects any extra keyword arguments into a dict.

```python
# basic tuple/list unpacking
a, b = (1, 2)         # a=1, b=2
x, y, z = [3, 4, 5]   # x=3, y=4, z=5

# starred (extended) unpacking
first, *middle, last = [1, 2, 3, 4, 5]  # first=1, middle=[2,3,4], last=5

# swap variables
a, b = b, a

# function call unpacking
def foo(x, y, z):
    print(x, y, z)

args = (1, 2, 3)
foo(*args)            # same as foo(1, 2, 3)

# dict unpacking / merging and kwargs
d1 = {"a": 1}
d2 = {"b": 2}
merged = {**d1, **d2}  # {'a':1, 'b':2}

def bar(**kwargs):
    print(kwargs)

bar(**{"x": 10})      # bar(x=10)
```

### map function

- its purpose to allow u to map every element and return a new array based from the original array

- map(func, iterable, \*more) calls func on each item and returns a lazy iterator (map object)

### passing a function difference

- in Python functions are objects (callable objects). You can pass, assign, store, and return them just like ints or strings.

wrong: this will call it immediately

```python
def add(sum(), n)
```

correct: pass funciton anme

```python
def add(sum, n1, n2)
    sum(n1,n2)
    sum(n1,n2)
    sum(n1,n2)
```

### list comprehension

A compact way to create a list by transforming and/or filtering an iterable using a single expression.

Syntax:

- [expression for item in iterable if condition]

```python
# basic: square numbers
squares = [x * x for x in range(5)]  # [0, 1, 4, 9, 16]
uppercased = [word.upper() for word in words]

# with a filter (only evens)
evens = [x for x in range(10) if x % 2 == 0]  # [0,2,4,6,8]

# nested (flattening a 2D list)
matrix = [[1,2],[3,4]]
flat = [v for row in matrix for v in row]  # [1,2,3,4]

# with enumerate (index + value)
pairs = [(i, v) for i, v in enumerate(["a","b","c"])]  # [(0,'a'), (1,'b'), (2,'c')]
```

### filter

The filter() method in Python is a built-in function used to filter elements of an iterable (like a list) based on a condition.

- filter(function, iterable)
- function → a function that returns True or False for each element.
- iterable → the sequence you want to filter (list, tuple, etc.).
- Returns a filter object (which you usually convert to a list or tuple).

```python
nums = [1, 2, 3, 4, 5, 6]

def is_even(n):
    return n % 2 == 0

result = filter(is_even, nums)
print(list(result))  # [2, 4, 6]

```

### dictionary comprehensions

- A dict comprehension builds a dict from an iterable using a compact expression.

{key_expr: value_expr for item in iterable if condition}

```python
# basic: squares
{s: s * s for s in range(5)}  # {0:0, 1:1, 2:4, 3:9, 4:16}

# from pairs
pairs = [("a", 1), ("b", 2)]
{k: v for k, v in pairs}  # {'a':1, 'b':2}

# swap keys/values
orig = {"a": 1, "b": 2}
{v: k for k, v in orig.items()}  # {1:'a', 2:'b'}

# with condition and expression
{x: ("even" if x % 2 == 0 else "odd") for x in range(6) if x > 0}
# {1:'odd', 2:'even', 3:'odd', 4:'even', 5:'odd'}

# nested loops (Cartesian-like)
{(i, j): i * j for i in range(3) for j in range(3)}
```

### enumerate

- this lets you loop a collection of data with a counter
- returns to value a index and the data of that index

```python
for index, value in enumerate(iterable, start=0):
```

### generators

allows us to generate amount of big data, usually when we for loop big amount of data it will take a long time or crash

- a solution for this is generators which allows us to generate bit by bit at a time

#### yield

this turns a function into a generator and it tells python to return one at a time from a loop

```python
# simple generator
def sheep(n):
    for i in range(n):
        yield "sheep" * i
```

#### iterators

- yield is returning a iterator that allow our own code in main to iterate over generated values one at a time
