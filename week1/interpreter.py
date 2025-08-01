def interpreter():
    a, b, c = input("Expression: ").split()
    a, c = float(a), float(c)
    if b == "+":
        return a + c
    elif b == "-":
        return a - c
    elif b == "*":
        return a * c
    elif b == "/":
        return a / c


print(interpreter())
