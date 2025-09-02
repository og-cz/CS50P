def main():
    string = input("Greeting: ")
    print(f"${value(string)}")


def value(string):
    string = string.lower().strip()
    if string.startswith("hello"):
        return "0"
    elif string.startswith("h"):
        return "20"
    else:
        return "100"


if __name__ == "__main__":
    main()
