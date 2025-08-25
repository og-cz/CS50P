## Libraries

- library is a files of code that other people have written that we can use on our program or we created that we can use so on
- A library is a collection of modules that provide related functionality.

we can share this using modules

common python libraries:
Data Science & Math: NumPy, Pandas, SciPy, SymPy
Machine Learning & AI: scikit-learn, TensorFlow, PyTorch, Keras
Data Visualization: Matplotlib, Seaborn, Plotly, Bokeh
Web Development: Flask, Django, FastAPI
Networking & Web Scraping: Requests, BeautifulSoup, Scrapy, Selenium
Utilities: OpenCV, Pillow, PyGame, SQLAlchemy

### modules

- modules in python is just a library that typically has one or more functions or feautures built in to it
- it is being used to promote reuseability of code

common python modules:
Math & Numbers: math, random, decimal, fractions
Data & Collections: collections, itertools, heapq, array
File & OS: os, sys, shutil, glob
Time & Date: time, datetime, calendar
Text & Data Processing: re, json, csv, string
Networking & Web: socket, http, urllib, requests
Others: logging, functools, pickle, argparse

### import

- import allow us to import the contents of some module in python

```python
import random # this import the whole file
random.choice([1,2,3])
```

### from

- from is a keyword in python to import a function in python so it's more specific
- no need to specify the random and just say choice

```python
from random import choice # it loads the function name of choice
choice([1,2,3])
```

### random library's functions

#### randint

- basically get back a random number from a to b inclusive

#### shuffle

- just shuffle the data we have and randomizes it

### statistics libraries

📊 Measures of Central Tendency

- `mean(data)`
- `fmean(data)` (faster, returns float)
- `geometric_mean(data)`
- `harmonic_mean(data)`
- `median(data)`
- `median_low(data)`
- `median_high(data)`
- `median_grouped(data, interval=1)`
- `mode(data)`
- `multimode(data)`

📉 Measures of Spread (Dispersion)

- `pstdev(data, mu=None)` (population standard deviation)
- `stdev(data, xbar=None)` (sample standard deviation)
- `pvariance(data, mu=None)` (population variance)
- `variance(data, xbar=None)` (sample variance)

### command-line arguments

A command-line argument is a way to pass information to a program when you run it from the terminal or command prompt. Instead of hardcoding values in your program, you can give them dynamically.

#### sys

sys is a built-in Python module that provides access to system-specific parameters and functions.

Some common uses:
sys.argv → access command-line arguments
sys.exit() → stop a program
sys.path → show paths where Python looks for modules

#### sys.argv

- argument vector basically just list of the all the word that human have prompt before it they had entered
- in short each word in sys.argv ends up in each element inside a list

so sys.aegv of 'hello world guys' would reuslt in ["hello", "world", "guys"]

#### sys.exit

- it will exit the program

### slices

Python slices are a very powerful way to extract parts of sequences like lists, strings, or tuples

Syntax:

```python
sequence[start:stop:step]
```

- `start` → starting index (inclusive, default 0)
- `stop` → ending index (exclusive)
- `step` → step size (default 1)

  > or

- start = 2 → inclusive, so it starts at index 2 → value 2
- stop = 5 → exclusive, so it stops before index 5 → last value is index 4 → value 4

**Examples:**

```python
numbers = [0,1,2,3,4,5,6] # basis

numbers[2:5]   # [2,3,4]      -> index 2 to 4
numbers[:4]    # [0,1,2,3]    -> start to index 3
numbers[3:]    # [3,4,5,6]    -> index 3 to end
numbers[::2]   # [0,2,4,6]    -> every 2nd element
numbers[::-1]  # [6,5,4,3,2,1,0] -> reversed
numbers[-3:]   # [4,5,6]      -> last 3 elements
numbers[:-3]   # [0,1,2,3]    -> all but last 3
```

**Strings work the same way:**

```python
text = "Python"
text[1:4]   # 'yth'
text[:3]    # 'Pyt'
text[::2]   # 'Pto'
text[::-1]  # 'nohtyP'
```

**Notes:**

- Slicing returns a **new sequence**, original stays intact.
- Negative indices count from the **end**.
- `step` can **skip** or **reverse** elements.

### packages

A package is a folder containing Python modules with an **init**.py file.

- package is a third party library said by David J. Malan

#### pyPI

- python package index = we can acess this using terminal or website in order to get packages

#### cowsay

- package in python that allows us to cow say something in our screen

#### pip

- package manager of python
- its a program that comes up withp python that allows us to install package in mac, pc or cloud environment in just one command and now we have access to a whole new library in python

```terminal
pip install cowsay

Collecting cowsay
Downloading cowsay-6.1-py3-none-any.whl.metadata (5.6 kB)
Downloading cowsay-6.1-py3-none-any.whl (25 kB)
Installing collected packages: cowsay
Successfully installed cowsay-6.1

[notice] A new release of pip is available: 25.1.1 -> 25.2
[notice] To update, run: python.exe -m pip install --upgrade pip
```

### APIs, request, JSON

#### APIs

Definition: An API is a set of rules, protocols, or tools that lets different software programs communicate with each other.

- API is an application programming interface = third party service that you and i write code that talk to
- not all but many api runs on internet
- we can write code that pretends to be a browser and connects to that 3rd party API and download some data taht we can incorporate in our own data

#### request

- requests libraries allows us to make web request

#### JSON

- javascript object notation = is typically used langauge agnostic format to exchange data in computer
- its a text based format in a standard way using curly braces, square brackets, and quotes and some colon that contains some information

# RECAP OF THE IMPORTANT THINGS TO UNDERSTAND!

- **import** → include a module or package in your code

  ```python
  import math
  print(math.sqrt(16))  # Output: 4.0
  ```

- **from** → import specific functions or classes from a module

  ```python
  from math import sqrt
  print(sqrt(25))  # Output: 5.0
  ```

- **modules** → single Python file (`.py`) containing code

  ```python
  # mymodule.py
  def greet():
      print("Hello!")
  ```

- **libraries** → collection of modules/packages providing functionality
  Example: NumPy is a library, it contains many modules like numpy.linalg, numpy.fft, etc.

  ```python
  # requests is a library
  import requests
  response = requests.get("https://api.github.com")
  print(response.status_code)
  ```

- **packages** → A package is a folder containing modules and a special file **init**.py.

The **init**.py file tells Python “this folder is a package” and can also run initialization code.

Think of a package as a library that has a folder structure, organizing modules neatly.

```python
mypackage/
│
├─ __init__.py       # marks it as a package
├─ module1.py
├─ module2.py
└─ subpackage/
    ├─ __init__.py
    └─ module3.py

then you can do:

import mypackage.module1
from mypackage.subpackage import module3
```

- **PyPI** → Python Package Index, repository of third-party packages

  ```bash
  # example: search and install packages from PyPI
  pip install requests
  ```

- **pip** → Python package installer

  ```bash
  pip install numpy
  ```

- **APIs** → Application Programming Interfaces for program communication

  ```python
  import requests
  response = requests.get("https://api.example.com/data")
  print(response.json())
  ```

- **request** → send a message to an API (commonly using `requests` library)

  ```python
  import requests
  response = requests.get("https://api.github.com")
  print(response.status_code)
  ```

- **JSON** → format for exchanging data (commonly used with APIs)

  ```python
  import json
  data = '{"name": "Alice", "age": 25}'
  parsed = json.loads(data)
  print(parsed["name"])  # Output: Alice
  ```

- **Custom libraries** → your own Python modules or packages for reuse

  ```python
  # mylib.py
  def hello(name):
      print(f"hello, {name}")

  # usage
  import mylib
  mylib.hello("David")  # Output: hello, David
  ```
