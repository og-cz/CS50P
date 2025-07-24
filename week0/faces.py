def faces(string = input()):
    string = string.replace(":)", "🙂")
    string = string.replace(":(", "☹️")
    return string

print(faces())