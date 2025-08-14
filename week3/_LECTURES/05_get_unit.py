def get_int():
    while True:
        try:
            return int(input("what is x? "))
        except ValueError:
            print("x is not a integer")


print(get_int())

print("another way")


def get_int(x):
    while True:
        try:
            x = int(input("what is x? "))
        except ValueError:
            print("x is not a integer")
        else:
            break
    return x


print(get_int())
