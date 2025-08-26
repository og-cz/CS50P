import pyfiglet
import sys
import random

# python figlet.py
# print(sys.executable) to know which python exectuable is running then get url + pip install

if len(sys.argv) == 1:
    # f = pyfiglet.Figlet()
    # fonts = f.getFonts()
    # font = random.choice(fonts)
    font = random.choice(pyfiglet.Figlet().getFonts())  # shorter
    setFont = pyfiglet.Figlet(font=f"{font}")
    text = input("Input: ")
    print("Output:", setFont.renderText(text))
elif len(sys.argv) == 3:
    two = sys.argv[1]
    font = sys.argv[2]
    if two in ["-f", "--font"] and font in pyfiglet.FigletFont.getFonts():
        setFont = pyfiglet.Figlet(font=f"{font}")
        text = input("Input: ")
        print("Output:", setFont.renderText(text))
    else:
        print("Invalid usage")
        sys.exit(1)
else:
    print("Invalid usage")
    sys.exit(1)
