def hello(name):
    print(f"hello, {name}")

hello("OG-CZ") 

# function that concat 2 strings
def concat(str1, str2):
    return str1 + str2

print(concat("C", "Z"))

# default value and multiple def
def hello(string="World"):
    print("hello,", string)

hello()


# outside() -> it NameError cause python interpreter reads upward to downward 
# so acessing a variable that is lower than the function is a error ; it must exist before we use it
# we can avoid it using scope






































def outside():
    print("it works")
