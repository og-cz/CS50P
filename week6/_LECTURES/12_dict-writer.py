import csv

name = input("whats ur name? ")
home = input("wheres ur home? ")

with open("dict-writer.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])  # return dictionaries
    writer.writerow({"name": name.rstrip(), "home": home.rstrip()})
