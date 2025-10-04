def main():
    yell("this", "is", "cs50")
    shout("this", "is", "cs50")
    times2(10, 50, 100)


def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


# same to map function
def shout(*words):
    uppercased = [word.upper() for word in words]  # compact way
    print(*uppercased)


def multply(n):
    return n * 2


def times2(*n):
    numbers = map(multply, n)
    print(*numbers)


main()
