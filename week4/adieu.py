import inflect

names = []

while True:
    try:
        name = input("Name: ")
        if name == "":
            raise EOFError
        names.append(name)
    except EOFError:
        break

p = inflect.engine()

print(f"Adieu, adiue, to {p.join(names)}")
