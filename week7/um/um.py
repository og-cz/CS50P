
import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    find = re.findall(r'\bum\b', s, re.IGNORECASE)
    if find:
        return len(find)
    return 0



if __name__ == "__main__":
    main()
