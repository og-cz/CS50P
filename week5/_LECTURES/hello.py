def main():
    name = input("Whats your name? ")
    print(hello(name))  # just turn into this


def hello(name="world"):
    # print("hello,", name) # culprit of error
    return f"hello, {name}"


if __name__ == "__main__":
    main()
