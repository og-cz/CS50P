for i in [0, 1, 2]:
    print(i)


for i in range(100):
    print(i)

# if we dont care if the variable not required the correct way of pythonic style is usign _
for _ in range(1):
    _ + 0

# pythonic way
# by default is end="\n" so what we did is end="" nothing
print("meow\n" * 3, end="")
