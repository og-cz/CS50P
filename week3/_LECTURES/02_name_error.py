try:
    x = int(input("what is x? "))
except ValueError and NameError:
    print("x is not an integer, Error")

print(f"letter is {x}")
