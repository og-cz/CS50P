
groceries = []


def grocery():
    while True:
        try:
            word = input().upper()
            groceries.append(word)
        except EOFError:
            groceries.sort()
            seen = []
            for items in groceries:
                if items not in seen:
                    print(items, groceries.count(items))
                    seen.append(items)
            break


grocery()
