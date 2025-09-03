students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        # or shorter way (below)
        # student = {"name": name, "house": house}
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)


for student in sorted(
    students, key=lambda student: student["name"]
):  # sort this list looking at this key
    print(f"{student['name']} is in {student['house']}")
