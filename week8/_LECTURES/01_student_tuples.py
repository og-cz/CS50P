
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
    if student[0].lower() == "padma":
        student[1] = "Ravenclaw"
    print(f'{student[0]} from {student[1]}') 

def get_student():
    name = 'pAdma'
    house = 'griffyndor'
    # return (name, house) # we are returning one value a tuple with 2 strings | immutable
    return [name, house ] # we are returnign a list | mutable

if __name__ == "__main__":
    main()