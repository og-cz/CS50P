def sheep(n):
    for i in range(n):
        yield "sheep" * i


# yield - its generating a little bit of data at a time

n = int(input("whats n? "))

for s in sheep(n):
    print(s)
