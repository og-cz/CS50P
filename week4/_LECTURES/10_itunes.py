import requests  # pyright: ignore[reportMissingModuleSource]
import sys
import json

# python 10_itunes.py weezer

if len(sys.argv) != 2:
    sys.exit()


response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=25&term=" + sys.argv[1])

print(json.dumps(response.json(), indent=2))

# or
object = response.json()
for result in object["results"]:
    print(f"Song: {result["trackName"]}")
