students = [
    {"name": "Harry Potter", "house": "Gryffindor"},
    {"name": "Hermione Granger", "house": "Gryffindor"},
    {"name": "Ron Weasley", "house": "Gryffindor"},
    {"name": "Draco Malfoy", "house": "Slytherin"},
    {"name": "Luna Lovegood", "house": "Ravenclaw"},
    {"name": "Cedric Diggory", "house": "Hufflepuff"},
]


# general syntax
# [expression for item in iterable if condition]
gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]  # this basically says choose the data of student name in students, only if student`s house is equals to gryffindor

for gryffindor in sorted(gryffindors):
    print(gryffindor)
