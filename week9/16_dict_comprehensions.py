students = ["hermione", "harry", "ron"]

gryffindors = []

for student in students:
    gryffindors.append({"name": student, "house": "gryffindors"})


print(gryffindors)

# or a compact way -> dict comprehensions

students = ["hermione", "harry", "ron"]
gryffindors = {student: "gryffindor" for student in students}
print(gryffindors)
