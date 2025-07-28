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
-> this one bar ( | )

🧬 Technical intuition:

> ( | ) is part of Python's Structural Pattern Matching introduced in Python 3.10.

It's inspired by functional languages like Haskell and Rust, where | is commonly used for pattern alternation.

It's not an expression that evaluates to a boolean, it's declarative pattern logic.
