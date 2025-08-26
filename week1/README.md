### takeaways

```python
def is_even(n):
    return True if n % 2 == 0 else False
```

i can see the same thing in java when it comes to pythonic expression

well, based from my research that it is called pythonic cause the core and principles of python is its conciseness and clarity

while we can actually do the same thing in java, but java concept is to be more explicit or statically typed

```java
static String isEven(int n) {
    return (n % 2 == 0) ? "Even" : "Odd";
}
```

important thing in match
# 📝 Python `match` Statement: Why Use `|` Instead of `or`

- `|` in `case` statements is used for **pattern matching**, not boolean logic.
- It means: **match any of these values**.
- `or` is a **boolean operator** that returns the **first truthy value**, not multiple patterns.

## ✅ Correct:
```python
match name:
    case "harry" | "hermione" | "ron":
        print("gryffindor")
