import re
url = 'https://www.twitter.com/davidjmalan'
# re.sub(pattern, repl, string, count=0, flags=0)

# we just make the https or www 0 or 1
# we make https? - https or http 

# subtitute
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url) 

print(username)