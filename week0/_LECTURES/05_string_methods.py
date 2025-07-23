name = "             OG-CZ           "

# remove whitespace from str
name = name.strip()

# capitalizes the first letter and make everything small
name = name.capitalize()

print("hello, " + name)

name = "david malan"

# capitalizes every individual word
name = name.title() 
print(name)

# a "better" way of doing it
name = "          david malan         ".strip().title()
print(f"hello, {name}")