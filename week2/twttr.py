def twitter():
    str = input("Input: ")
    word = ""
    for i in str:
        if i.lower() not in 'aeiou':
            word += i

    return f"Output: {word}"


print(twitter())
