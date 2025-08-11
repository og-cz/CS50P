import re


def camel_case():

    word = input("camelCase: ")
    parts = []
    combine = ""

    for i in word:
        if i.isupper():
            parts.append(combine)
            combine = ""
            combine += i.lower()
        else:
            combine += i.lower()

    parts.append(combine)
    word = "_".join(parts)

    return word


print(camel_case())
