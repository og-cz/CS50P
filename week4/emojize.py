# emoji : https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias

emoji_dictionaries = {
    ":1st_place_medal:": "🥇",
    ":thumbsup:": "👍",
    ":thumbs_up:": "👍",
    ":earth_africa:": "🌍",
    ":earth_americas:": "🌎",
    ":earth_asia:": "🌏",
    ":money_bag:": "💰",
    ":smile_cat:": "😸",
    ":candy:": "🍬",
    ":ice_cream:": "🍨",
}


def emojize():
    result = input("Input: ").strip()

    emoji = ""
    state = False
    output = ""

    for char in result:
        if char == ':' and not state:
            emoji += char
            state = True
        elif char == ':' and state:
            emoji += char
            output += emoji_dictionaries.get(emoji)
            emoji = ""
            state = False
        elif state:
            emoji += char
        else:
            output += char

    return output


print(emojize())
