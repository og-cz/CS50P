import random
import sys

while True:
    level = input("Level: ")
    if level.isdigit() and int(level) > 0:
        level = int(level)
        break

random_number = random.randint(1, level)

while True:
    guess = input("Guess: ")

    if not guess.isdigit():
        continue

    guess = int(guess)

    if guess <= 0:
        continue

    if guess > level:
        print("Too large!")
        continue

    if guess < random_number:
        print("Too small!")
    elif guess > random_number:
        print("Too large!")
    else:
        print("Just Right!")
        sys.exit(0)
