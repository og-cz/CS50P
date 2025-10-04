students = [
    {"name": "Harry Potter", "house": "Gryffindor"},
    {"name": "Hermione Granger", "house": "Gryffindor"},
    {"name": "Ron Weasley", "house": "Gryffindor"},
    {"name": "Draco Malfoy", "house": "Slytherin"},
    {"name": "Luna Lovegood", "house": "Ravenclaw"},
    {"name": "Cedric Diggory", "house": "Hufflepuff"},
]


def is_gryffindor(s):
    return s["house"] == "Gryffindor"


gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(
    gryffindors, key=lambda s: s["name"]
):  # its just a way to sort based of student
    print(gryffindor["name"])
