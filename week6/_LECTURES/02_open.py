name = input("whats ur name? ")

file = open("02_open.txt", "a")
file.write(f"{name}\n")
file.close()
