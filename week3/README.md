# CS50p Week 3

- [Syntax Error](#syntax-error)
- [Value Error](#value-error)
- [`try`](#try)
- [`except`](#except)
- [Name Error](#name-error)
- [else](#else)
- [pass](#pass)

### Syntax Error

```python
print("abc)
```

- A problem in the code’s structure/format (typing mistake, missing quotes, brackets, etc.).
- Python catches this before running the program.

---

### Value Error

```python
x = int(input("Enter: "))  # Example input: "x"
```

- Happens when the value is the wrong type for an operation.
- Example: entering text when an integer is expected.

---

### `try`

- Used to run code that _might_ cause an error.
- Lets you handle the error gracefully without crashing the program.

---

### `except`

- Runs if an error happens in the `try` block.
- Can handle specific error types (e.g., `ValueError`, `NameError`).

---

### Name Error

- Happens when you use a variable that was never created or initialized.
- Common when:

  - A variable assignment never completed because of an error.
  - The variable is referenced before it’s defined.

```python
try:
    x = int("a")  # This fails
except ValueError:
    print("Error happened")

print(x)  # NameError: x is not defined
```

```

Do you want me to also **add a small diagram showing the try–except flow** so it’s easier to remember? That would make your notes more visual.
```

### else

```python
try:
    x = int(input("what is x? "))
except ValueError:
    print("x is not an integer, ValueError")
else:
    print(f"letter is {x}")
```

TRY successful → go to ELSE

TRY failed → go to EXCEPT

### pass

In Python, pass is a do nothing statement, it’s literally a placeholder.
