def deep(reply=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()):
    if (reply == "42" or reply == "forty-two" or reply == "forty two"):
        print("Yes")
    else:
        print("No")


deep()
