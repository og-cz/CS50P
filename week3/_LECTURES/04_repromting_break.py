while True:
    try:
        x = int(input("what is x? "))
    except ValueError:
        print("x is not a integer")
    else:
        break

print(f"x is {x}")

print("another way to do")

while True:
    try:
        x = int(input("what is x? "))
        break
    except ValueError:
        print("x is not a integer")


print(f"x is {x}")
