students = ["hermione", "harry", "ron"]

for i in range(len(students)):
    print(i + 1, students[i])

print()  # or a enumerate way

for i, student in enumerate(students, start=1):
    print(i, student)
