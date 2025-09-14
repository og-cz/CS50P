import sys
from PIL import Image, ImageOps
import os

#  python shirt.py before1.jpg after1.jpg
if len(sys.argv) == 3:
    extensions = [".jpg", ".jpeg", ".png"]
    extension1 = os.path.splitext(sys.argv[1])
    extension2 = os.path.splitext(sys.argv[2])

    if extension1[1] == extension2[1] and extension1[1] in extensions:
        try:
            user_image = Image.open(input)
        except FileNotFoundError:
            sys.exit("File doesn't exist")

        shirt = Image.open("shirt.png")
        size = shirt.size  # (width, height) returns a tuple .size
        user_image = ImageOps.fit(
            user_image, size
        )  # we resize the before1 image bcs to fit the shirt for after1 image
        user_image.paste(shirt, shirt)
        user_image.save(sys.argv[3])
        sys.exit(1)
    elif extension1[1] != extension2[2]:
        sys.exit("input and output have different extensions")
    else:
        sys.exit("wrong extension")
elif len(sys.argv) > 3:
    sys.exit("too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("too few command-line arguments")
