
# tuple example - immutable list code below 
tuple = (1, 2, 3) # parentheses are optional
# tuple[0] = 8 # this will give an error as tuples are immutable

# list example - mutable
list = [1, 2, 3] 
# list[0] = 8 # this will work as lists are mutable

# dictionary example - mutable with key value pairs
dictionary = {"name": "padma", "house": "gryffindor"}
# dictionary["name"] = "hermione" # this will work as dictionaries are mutable

def main():
    student = get_student()
    if student['name'] == 'padma':
        student['house'] = 'ravenclaw'
    print(f'{student['name']} from {student['house']}') 

def get_student():
    student = {}
    student['name'] = 'padma'
    student['house'] = 'gryffindor'
    return student

    # or 
    # name = 'padma'
    # house = 'gryffindor'
    # return {'name': name, 'house': house}

if __name__ == "__main__":
    main()