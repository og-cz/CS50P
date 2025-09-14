import re
url = 'https://www.twitter.com/davidjmalan.mad'

# -> (.+$) = THIS IS USED TO CAPTURE SPECIFIC USERNAME

# -> (?:www\.) the ?: meaning we dont have to extract it so instead of group 2 we can just use group 1
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_.]+)", url ,re.IGNORECASE):
    username = matches.group(1) # just group 1 cause of :?

print(username)