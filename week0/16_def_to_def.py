def main():
    string = input("What's your name? ")
    hello(string)

# main() -> this error cause still it hello() doesnt exists before main()


# def hello(): -> error cause TypeError: hello() takes 0 positional arguments but 1 was given
def hello(string="World"):
    print("Hello,", string)

main()