def sheep(n):
    flock = []
    for i in range(n):
        flock.append("sheep" * i)
    return flock


# it will take alot of time if we have enormous n of data
# and if we input 1_000_000 it might crash

n = int(input("whats n? "))

for i in range(n):
    print("sheep" * i)


for s in sheep(n):
    print(s)
