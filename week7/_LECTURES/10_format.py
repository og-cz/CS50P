import re

name = "malan, david"

if ',' in name:
    last,first = name.split(', ') # not applicable for regex and only fixes already reversed word 
    name = f"{first} {last}"

print(f"hello, {name}")