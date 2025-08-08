students = [
    {"name": "hermione", "house": "gryffindor", "group": "group1"},
    {"name": "harry", "house": "gryffindor", "group": "group2"},
    {"name": "ron", "house": None, "group": "group2"}
]

for _ in students:
    print(_["name"], _["house"], _["group"], sep=", ")
