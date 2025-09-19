import re

def parse(s):
    if '<iframe' not in s:
        return None

    try:
        # extract src attribute
        src = re.search(r'src="([^"]+)"', s).group(1)
        if not re.match(r'^https?://(www\.)?youtube\.com/embed/', src):
            return None
        video_id = src.split("/embed/")[1]
    except AttributeError:
        return None
    else:
        return f"https://youtu.be/{video_id}"
