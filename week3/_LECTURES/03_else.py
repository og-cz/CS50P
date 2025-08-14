try:
    x = int(input("what is x? "))
except ValueError:
    print("x is not an integer, ValueError")
else:
    print(f"letter is {x}")
