import csv

name = input("whats ur name? ").rstrip()
home = input("wheres ur home? ").rstrip()

with open("list-writer.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
