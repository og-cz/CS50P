name = "drAcO"


match str.lower(name):
    case "harry":
        print("griffindor")
    case "hermione":
        print("gryffindor")
    case "ron":
        print("gryffindor")
    case "draco":
        print("slytherin")
    case _:
        print("who?")

match str.lower(name):
    case "harry" | "hermione" | "ron":
        print("gryffindor")
    case "draco":
        print("slytherin")
    case _:
        print("who?")
