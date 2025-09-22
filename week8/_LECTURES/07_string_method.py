class Student:
    def __init__(self, name, house):
        if not name: 
            raise ValueError('missing name') 
        self.name = name
        self.house = house

    def __str__(self):
        return f'{self.name} from {self.house}' # the string method

def main():
    student = get_student()
    print(student)

def get_student():
    name = 'draco'
    house = 'slytherin'
    if house not in ['gryffindor', 'hufflepuff', 'ravenclaw', 'slytherin']: 
        raise ValueError('invalid house')
    return Student(name, house) 


if __name__ == "__main__":
    main()