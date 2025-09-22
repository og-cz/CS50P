class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    @classmethod # i can call this method without instanciating Student()
    def get(cls):
        name = 'harry'
        house = 'gryffindor'
        return cls(name,house)

def main():
    student = Student.get()
    print(f'{student.name} from {student.house}')



if __name__ == "__main__":
    main()