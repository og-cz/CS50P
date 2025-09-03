name = input("whats ur name? ")

with open("03_with.txt", "a") as file:
    file.write(f"{name}\n")
