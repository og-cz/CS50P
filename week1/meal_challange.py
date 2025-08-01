def main():
    time = input("What time is it? ")
    time = convert(time)

    if time >= 7.0 and time <= 8.0:
        print("breakfast time")
    elif time >= 12.0 and time <= 13.0:
        print("lunch time")
    elif time >= 18.0 and time <= 19.0:
        print("dinner time")


def convert(time):

    if time.endswith("a.m.") or time.endswith("p.m."):
        a, meridian = time.split(" ")
        hours, minutes = a.split(":")
        hours = float(hours)
        minutes = float(minutes) / 60

        if meridian == "a.m.":
            if hours == 12:
                hours = 0
        elif meridian == "p.m.":
            if hours != 12:
                hours += 12

        return hours + minutes

    else:
        hours, minutes = time.split(":")
        minutes = float(minutes) / 60
        return float(hours) + minutes


if __name__ == "__main__":
    main()
