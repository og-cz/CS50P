with open("03_with.txt", "r") as file:
    lines = file.readlines()

for line in lines:  # lines is a list which automatically read by line
    print("word =", line.rstrip())
    # or print("word =", line, end="") # same thing


# or simpler way

with open("03_with.txt", "r") as file:
    for line in file:
        print("halo,", line.rstrip())
