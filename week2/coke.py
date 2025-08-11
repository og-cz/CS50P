def coke():
    due = 50
    while due != 0:
        print("Amount Due:", due)
        insert = int(input("Insert Coint: "))

        if insert in [25, 10, 5]:
            due -= insert

    if due < 0:
        return f"Change Owed: {-due}"
    else:
        return "Chaned Owed: 0"


print(coke())
