def main():
    x, y = input("Fractions: ").split("/")
    while True:
        try:
            result = convert(x, y)
            output = gauge(result)
            print(output)

            break
        except TypeError as e:
            continue


def convert(x, y):
    try:
        x, y = int(x), int(y)
    except ValueError:
        raise ValueError("Inputs must be integers")

    if y == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    if x < 0 or y < 0 or x > y:
        raise ValueError("Invalid fraction")

    return int(round((x / y) * 100))


def gauge(result):
    if result <= 1:
        return "E"
    elif result >= 99:
        return "F"
    else:
        return f"{round(result)}%"


if __name__ == "__main__":
    main()
