class Student:
    ...
    
def main():
    student = get_student()
    print(f'{student.name} from {student.house}')

def get_student():
    student = Student() # instance of a class Student() under object student
    student.name = 'harry' # instance variable of student object
    student.house = 'gryffindor' # instance variable of student object
    return student

# or 
    # name = input('name: ')
    # house = input('house: ')
    # student = Student(name, house)
    # return student
if __name__ == "__main__":
    main()