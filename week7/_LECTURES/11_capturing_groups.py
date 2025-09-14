import re

name = "malan, david"

matches = re.search(r"^(.+), (.+)$",name) # when u specify a group everything will be return to you as a individual value

print('matches:', matches)

if matches: # "Did the regex return a pattern match object (True) or None (False)?"
    
    # last, first = matches.groups() # this returns the individual groups captured
    # name = matches.group(2) + " " + matches.group(1)
    
    # same as the top code
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"

print(f"hello, {name}")