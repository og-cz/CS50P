# mypy 05_type_hints.py


def meow(n: int) -> str:
    return "meow\n" * n


number: int = int(input("number:"))
meows: str = meow(number)
print(meows)
