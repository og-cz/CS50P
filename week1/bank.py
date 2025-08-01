def greeting(string=input("Greeting: ").lower().strip()):
    if string.startswith("hello"):
        return "0"
    elif string.startswith("h"):
        return "20"
    else:
        return "100"


print(f"${greeting()}")
