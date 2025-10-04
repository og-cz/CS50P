# CS50p Week 8

- [OOP](#oop)
- [tuple](#tuple)
- [dictionary](#dictionary)
- [summary](#summary)
- [classes](#classes)
- [objects](#objects)
- [instance variables and attribtues](#instance-variables-and-attribtues)
- [methods](#methods)
- [\_\_init\_\_](#__init__)
- [raise](#raise)
- [string method \_\_str\_\_](#string-method-__str__)
- [properties](#properties)
  - [decorators](#decorators)
  - [@property](#property)
- [getter and setter in python explained](#getter-and-setter-in-python-explained)
- [types and classes](#types-and-classes)
- [class methods](#class-methods)
- [inheritance](#inheritance)
- [operator overloading](#operator-overloading)

### OOP

- object oriented programming
  in programming there is some paradigm
  so everything we did before is procedural everything is top to bottom
  another paradigm is OOP

### tuple

- is a collection of value in python
  like x, y, z
  similar to list and its immutable or we cant change value

### dictionary

- its a collection of keys and value

##### summary

```python
# tuple example - immutable list code below
tuple = (1, 2, 3) # parentheses are optional
# tuple[0] = 8 # this will give an error as tuples are immutable

# list example - mutable
list = [1, 2, 3]
# list[0] = 8 # this will work as lists are mutable

# dictionary example - mutable with key value pairs
dictionary = {"name": "padma", "house": "gryffindor"}
# dictionary["name"] = "hermione" # this will work as dictionaries are mutable
```

### classes

- isnt its great if the python people have something created liek a student data type itself
  a class is like a blueprint of pieces of a data, its like a mold that we can define and give a name
  and if we use this mold or blueprint its design to what we want

- classes is created for us to create our data type using classes

### objects

anytime we use a class we are creating somethin called objects
we create objects from classes

- class is a creation of a new data type
- object is the instanciation of class

```python
def get_student():
    student = Student()
    student.name = 'harry'
    student.house = 'gryffindor'
    return student
```

#### instance variables and attribtues

> technically, are really just variables name and house inside of a object whos type is Student

Instance variables are variables that belong to a specific object of a class. We usually create them inside \_\_init\_\_() using self. Each object gets its own copy

### methods

When you create a class in Python:

- You can define your own methods.
- Some methods are special/built-in, also called dunder (double underscore) methods.

#### \_ \_init\_ \_

- This is a special method that runs automatically when you create an object.
- It’s called the constructor in other languages (like Java, C++).

#### raise

- its just a exception that we can manually raise ur own exception when something's go wrong

### string method \_ \_str\_ \_

- special method when we define it in a class, python will automatically call this anytime some functions want to see our object as a string

Without **str**, printing an object would just show something like:

```python
<**main**.Student object at 0x0000012345ABCD>
```

With **str**

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

s = Student("Harry", "Gryffindor")
print(s)            # calls __str__ automatically
print(str(s))       # also calls __str__

OUTPUTS:
# Harry from Gryffindor
# Harry from Gryffindor
```

### properties

- this is just use to modify the functions behaviour, on how they apply
  and this properties are handle by what we call decorators

#### decorators

- this is the classification for the properties which includes @property, @name.setter, @staticmethod

#### @property

- this just turns a method into a getters

```python
class Student:
    def __init__(self, name):
        self._name = name

    @property       # decorator
    def name(self): # getter
        return self._name

    @name.setter    # decorator
    def name(self, value):  # setter
        if not value:
            raise ValueError("Name cannot be empty!")
        self._name = value
```

### getter and setter in python explained

```python
    # constructor
    def __init__(self, name, house):
        if not name:
            raise ValueError('missing name')
        self.name = name
        self.house = house

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
```

- if we look at the decorator we can see its linked up to @house and this is good because it means we can change anytime we want
- @property is always tied up to @house.setter if they have same house() function name
  which means: it ensure it access the same data
- \_house is just a way to not class self.house with **init**(house) because it will not run
- but still at the end of the day what ever name, it all boils down the the decorator which change the functionalities of a function in terms of accessability

### types and classes

- int and str are classes and object
  class int(x, base=10)
  class str(object='')

anytime we have force the string to lower case like str.lower()
we have taked the object str to convert everything to lower

so in short there, it has been always str is a instance of a class
and instance of string are objects that has function built in

additional:
list are also a class

- class list([iterable])
  inside this class are functions like append
- list.append(x)

### class methods

@classmethod - a way to access class variables and not instance variables
or access a method without instanciating a class()

> def test(cls, x):

The main difference between instance methods, class methods, and static methods is how they access data:
| Method Type | First Parameter | Can Access Instance Variables? | Can Access Class Variables? | Purpose / Use Case |
| --------------- | --------------- | ------------------------------ | --------------------------- | ----------------------------------------------------------------------------------- |
| Instance method | `self` | Yes | Yes | Works on one object (most common) |
| Class method | `cls` | No | Yes | Works on the class itself; often for class-wide changes or alternative constructors |
| Static method | None | No | No | Independent utility function inside a class |

### inheritance

to design our class in hiearacly fashion or barrow attributes, methods, variables in a class if they all have those in common

whereby we can define multiple classes that relates to each other, there can be some hierachy between them

### operator overloading

we can take symbols such as plus, minus, or other syntax in a keyboard and we can implement our own interpetation there of
