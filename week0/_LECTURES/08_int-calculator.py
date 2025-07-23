a = input("Input first number: ")
b = input("Input second number: ")
# c = a + b # this error cause we used + sign so it concatinated but really by default input -> is a string
c = int(a) + int(b)

print(c)

# same

a = 1
b = 1
c = a + b
print(c)