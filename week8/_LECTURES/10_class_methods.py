import random
class Hat:
    # class variables, it shared same object across all instance of a class
    houses = ['gryffindor','hufflepuff','ravenclaw','slytherin']

    @classmethod
    def sort(cls, name): # cls -> class 
        print(name, 'is in', random.choice(cls.houses)) 

Hat.sort('harry')