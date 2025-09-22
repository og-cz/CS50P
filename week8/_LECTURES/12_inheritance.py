class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError('Missing name')
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
    
    ...

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    
    ...

wizard = Wizard('albus')
student = Student('Harry', 'Gryffindor')
professor = Professor('serverus', 'defense against the dark arts')

print(wizard.name)
print(student.name, student.house)
print(professor.name, professor.subject)

# output
# albus
# Harry Gryffindor
# serverus defense against the dark arts