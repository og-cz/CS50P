# in the python community that is smiled upon other languages
'''
Why is the first version more Pythonic?

Because in Python, clarity and conciseness are core values of the language. It’s part of the "Zen of Python" (you can try import this in a Python REPL to see it).
'''
def is_even(n):
    return True if n % 2 == 0 else False

print(is_even(10))

def is_even(n):
    return n % 2 == 0

print(is_even(6))