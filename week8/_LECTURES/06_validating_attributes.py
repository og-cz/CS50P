class Student:
    def __init__(self, first, middle, last, house=None):
        self.first = first
        self.middle = middle
        self.last = last
        if house not in ['gryffindor', 'hufflepuff', '']:
            raise ValueError('Invalid house')
        self.house = house

def main():
    student = get_student()
    

def get_student():
    first = 'harry'
    middle = 'potter'
    last = 'doe'
    house = ''
    return Student(first, middle, last, house) 


if __name__ == "__main__":
    main()