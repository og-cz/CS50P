class Student:
    def __init__(self, name, house, patronus):
        if not name: 
            raise ValueError('missing name') 
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f'{self.name} from {self.house}'
    
    def charm(self):
        match self.patronus:
            case 'stag':
                return 'yehaa!'
            case 'otter':
                return 'skadoosh'
            case 'jack ruseel terrier':
                return 'woof!'
            case _:
                return 'no patronus'

def main():
    student = get_student()
    print('expecto patronum')
    print(student.charm())

def get_student():
    name = 'draco'
    house = 'slytherin'
    patronus = 'stag'
    if house not in ['gryffindor', 'hufflepuff', 'ravenclaw', 'slytherin']: 
        raise ValueError('invalid house')
    return Student(name, house, patronus) 


        
if __name__ == "__main__":
    main()