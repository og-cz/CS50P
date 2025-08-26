from operator import le
import random


def main():
    level = get_level()
    score = 0
    tries = 0
    ten = 10

    while ten > 0:
        x = generate_integer(level)
        y = generate_integer(level)

        correct_answer = x + y
        tries = 0

        while tries < 3:
            answer = input(f"{x} + {y} = ")

            try:
                if int(answer) == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1

        if tries == 3:
            print(f"{x} + {y} = {correct_answer}")

        ten -= 1

    print(f"Score: {score}")


def get_level():
    while True:
        level = input("Level: ")
        try:
            if level == "1":
                return int(level)
            elif level == "2":
                return int(level)
            elif level == "3":
                return int(level)
            else:
                raise ValueError
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
