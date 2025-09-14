# coolest name ever i think...
import re

name = "malan, david"

if matches := re.search(r"^(.+), (.+)$",name): # when u specify a group everything will be return to you as a individual value
    name = matches.group(2) + " " + matches.group(1)


print(f"hello, {name}")