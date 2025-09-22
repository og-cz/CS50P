class Student:
    def __init__(self,  name, house):
        if not name: # raise exception
            raise ValueError('missing name') # control over correcrtness! 
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f'{student.name} from {student.house}')

def get_student():
    name = 'harry'
    house = 'gryffindor'
    if house not in ['gryffindor', 'hufflepuff', 'ravenclaw', 'slytherin']: # control over correcrtness! 
        raise ValueError('invalid house')
    return Student(name, house) 


if __name__ == "__main__":
    main()