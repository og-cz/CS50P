import csv

students = []  # dictionaries

import csv

with open("students.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        # print(row)
        print()


with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "home": row[1]})

for student in sorted(
    students, key=lambda student: student["name"]
):  # sort this list looking at this key
    print(f"{student['name']} is in {student['home']}")
