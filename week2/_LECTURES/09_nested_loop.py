from re import S


def main():
    print_square(3)


def print_square(size):
    # row
    for i in range(size):
        # column
        for j in range(3):
            print("#", end="")
        print()


main()
print()


def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        print("#" * size, end="")
        print()


main()
