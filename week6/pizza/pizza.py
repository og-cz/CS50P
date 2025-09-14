import csv
import sys
from tabulate import tabulate

# python pizza.py regular.csv

data = []
filename = sys.argv[1]

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)

if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)

if not filename.endswith(".csv"):
    print("Not a CSV file")
    sys.exit(1)

with open(filename, "r") as file:

    for line in file:
        pizza, small, large = line.strip().split(",")
        row = [pizza, small, large]
        data.append(row)

try:
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        print(tabulate(reader, headers="keys", tablefmt="grid"))
except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)
