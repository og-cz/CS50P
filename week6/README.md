# file I/O

so everything we do or program we written stores eveything in memory on runtime but anything we exit after it its lost but with file we can hang on to data long term so, File I/O in context of programming is read from and write to save information sa files itself

### lists number = [1,2,3]

unfotunately this stores in computer's memory, so we can save the information using File I/O

### open

there is a function called open, so its open a file which we can read and write a information on it
Think of it like unlocking a file and telling Python how you want to interact with it.

> link: https://docs.python.org/3/library/functions.html#open

```python
file_object = open("filename", mode)
```

- "filename" → the name or path of the file (e.g., "data.txt").
- mode → tells Python what you want to do with the file.

common modes
| Mode | Meaning |
| ----- | ------------------------------------------------------------------------ |
| `"r"` | **Read** (default). Opens file for reading. Error if file doesn’t exist. |
| `"w"` | **Write**. Creates a new file or overwrites if it already exists. |
| `"a"` | **Append**. Opens file for writing but adds new data to the end. |
| `"x"` | **Exclusive creation**. Creates new file; error if file exists. |
| `"b"` | **Binary mode** (e.g., `"rb"`, `"wb"` for images, audio). |
| `"t"` | **Text mode** (default, e.g., `"rt"`). |
| `"+"` | **Update mode**. Allows reading and writing (`"r+"`, `"w+"`, `"a+"`). |

### with

- When you open a file with open(), you need to close it manually using .close().
- If you forget, the file stays open, which can cause memory leaks or prevent other programs from accessing it.

```python
f = open("hello.txt", "r")
data = f.read()
print(data)
f.close()   # You MUST remember this
```

If your program crashes before f.close(), the file stays open. ❌

```python
with open("hello.txt", "r") as f:
    data = f.read()
    print(data)
# File is closed automatically here ✅
```

- with handles entering (opening the file) and exiting (closing it) safely.
- Even if there’s an error inside the block, the file will still close properly.

syntax

```python
with expression as variable:
    # code block
```

- expression → something that returns a context manager (like open()).
- variable → the object you’ll use inside (like f for the file).

### sorted

In Python, sorted() is a built-in function that returns a new sorted list from any iterable (like lists, tuples, strings, sets, or even dictionaries).

Basic Syntax

```python
sorted(iterable, key=None, reverse=False)
```

iterable → what you want to sort (list, tuple, string, etc.)
key → a function that decides how to sort each element
reverse → if True, sorts in descending order (default is ascending)

### comma-seperated values

what if we wanna store more values? in one line?
so there is something we call as .csv

CSV = Comma-Separated Values
It’s a simple text file format used to store data in a table-like structure (rows and columns).

- Each line = one row of data
- Each value inside the row = separated by a comma

Example: students.csv

```code
Name,Age,Grade
Alice,20,A
Bob,21,B
Charlie,19,C
```

- First row = headers (column names)
- Next rows = data

Why use CSV?

- Super simple and human-readable
- Works across almost all software (Excel, Google Sheets, Python, databases, etc.)
- No fancy formatting → just raw data

### key

- When you sort in Python, the computer needs to know:
- ➡️ “When comparing two items, what value should I use to decide their order?”
- That’s what the key parameter answers.

Another example
Sort by length of words:

```python
words = ["pear", "apple", "banana"]
print(sorted(words, key=len))
```

- Python takes each word, runs len(word)
- So it’s comparing: 4, 5, 6
- Output: ['pear', 'apple', 'banana']

general theory:
The key function transforms each element into something that can be compared easily.
Sorting then happens on that transformed value, not the original object.

### Lambda Function

- A lambda expression is basically a short way to write a function without giving it a name.
  It’s often called an anonymous function because you don’t define it with def (in Python) or public void (in Java) like normal functions/methods.

- General Idea
  A normal function:

```python
def square(x):
    return x * x
```

Same thing with a lambda expression:

```python
square = lambda x: x * x
```

Here, lambda x: x _ x means "a function that takes x and returns x _ x."

```python
lambda arguments: expression
```

- lambda → keyword that tells Python: "I’m making a lambda function"
- arguments → the parameters you pass in (like x, or a, b)
- : → separates the arguments from the body
- expression → must be a single expression, this is what the function returns

### csv library

The csv library is a built-in Python module that helps you read from and write to CSV (Comma-Separated Values) files.

- they created this because of past problems about csv now its a library
  > links: https://docs.python.org/3/library/csv.html

### csv reader

csv.reader(file) => its function is to read a file and figure out where is the comma or quotes or what is the potential corner case

Syntax

```python
csv.reader(file, delimiter=',')
```

- file → the file object (opened with open(...))
- delimiter → character that separates values (default is ,, but you can use \t for tabs, ; for semicolons, etc.)

### csv.DictReader

csv.DictReader is like csv.reader, but instead of giving you each row as a list, it gives you each row as a dictionary (where the keys are taken from the header row of the CSV).

So you don’t need to manually do:

```python
{"name": row[0], "home": row[1]}
```

Key difference:

- csv.reader → gives list rows (['Alice', 'New York'])
- csv.DictReader → gives dict rows ({'name': 'Alice', 'home': 'New York'})

### csv.writer

- csv.writer lets you write rows of data into a CSV file.

Each row you give it (as a list/tuple) will become a line in the CSV.

### csv.DictWriter

It’s part of Python’s built-in csv library.
- While csv.writer writes lists/tuples into a CSV file…
- csv.DictWriter writes dictionaries into a CSV file.
You give it a dictionary, it looks at the keys and writes values in the right columns.

### pillow library

Pillow is a Python imaging library.
It’s basically an improved version of the old PIL (Python Imaging Library).
With Pillow, you can easily open, edit, create, and save images in many formats (JPEG, PNG, GIF, etc.).

Why use it?

Because Python by itself can’t handle images directly — Pillow makes image processing simple:
Open and view images
Resize, crop, rotate
Convert between formats (e.g., JPG → PNG)
Add text, shapes, filters
Handle transparency
Even pixel-level editing