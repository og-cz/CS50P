import csv

students = []

with open("dict-students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)
        print(row["name"], row["home"])

for student in students:
    print(student)
