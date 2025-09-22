class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house # we cant do def house and __init__(house) because it collides so we can do _self

    def __str__(self):
        return f'{self.name} from {self.house}'
    
    # getter
    @property # decorator
    def house(self):
        return self._house
    
    # setter
    @house.setter # decorator
    def house(self, house):
        if house not in ['gryffindor', 'hufflepuff', 'ravenclaw', 'slytherin']: 
            raise ValueError('Invalid house')   
        self._house = house

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError('Missing name')
        self._name = name


def main():
    student = get_student()
    student.house = 'number four, privet drive' # invalid error because we changed it before get_student() = draco but we have # student.house = this name = Invalid House ERROR 
    student.name = 'new name'
    print(student)

def get_student():
    name = 'draco'
    house = 'slytherin'
    return Student(name, house) 


if __name__ == "__main__":
    main()