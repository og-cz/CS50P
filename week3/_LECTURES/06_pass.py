def get_int():
    while True:
        try:
            return int(input("what is x? "))
        except ValueError:
            pass


print(get_int())
