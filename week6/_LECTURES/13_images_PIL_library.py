import sys
from PIL import Image

images = []
# python costume.py costume1.gif costume2.gif

for arg in sys.arv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costume.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
