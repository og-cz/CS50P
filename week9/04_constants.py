MEOWS = 3

for _ in range(MEOWS):
    print("meow")

print()
# or


class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")


cat = Cat()
cat.meow()
cat.MEOWS = 2
print(cat.MEOWS)
