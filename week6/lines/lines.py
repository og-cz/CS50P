import sys

# python lines.py

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)

if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)

filename = sys.argv[1]

if not filename.endswith(".txt"):
    print("Not a Python file")

try:
    with open(filename) as file:
        for line in file:
            print(line, end="")
except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)
