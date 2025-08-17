def fuel():

    while True:
        try:
            x, y = input("Fractions: ").split("/")
            x, y = int(x), int(y)

            if y == 0 or x < 0 or y < 0 or x > y:
                raise ValueError

            result = (x / y) * 100
            if result <= 1:
                print("E")
            elif result >= 99:
                print("F")
            else:
                print(f"{round(result)}%", end="")
            break
        except (TypeError, ZeroDivisionError, ValueError) as e:
            pass


fuel()
