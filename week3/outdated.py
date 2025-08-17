from calendar import c
from os import remove, replace


month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def outdated():
    while True:
        date = input("Date: ")

        if "/" in date:
            try:
                m, d, y = date.strip().split("/")
                if 1 <= int(m) <= 12 and 1 <= int(d) <= 31 and y.isdigit():
                    m = m.zfill(2)
                    d = d.zfill(2)
                    y = y.zfill(4)
                    print(f"{y}-{m}-{d}")
                    break
            except ValueError:
                continue

        if "," in date:
            try:
                m, d, y = date.strip().split()
                m = m.title()
                d = d.replace(",", "")
                month_num = month.index(m) + 1

                if 1 <= int(m) <= 12 and 1 <= int(d) <= 31:
                    m = str(month_num).zfill(2)
                    d = d.zfill(2)
                    y = y.zfill(4)
                    print(f"{y}-{m}-{d}")
                    break
            except ValueError:
                continue


outdated()
