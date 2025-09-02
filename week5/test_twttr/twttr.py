def main():
    str = input("Input: ")
    word = shorten(str)
    print('output: ', word)


def shorten(str):
    word = ""
    for i in str:
        if i.lower() not in "aeiou":
            word += i

    return word


if __name__ == "__main__":
    main()
