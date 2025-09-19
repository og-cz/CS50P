import re
import sys


def main():
    try:
        print(validate(input("IPv4 Address: ")))
    except EOFError:
        pass



def validate(ip):
    if not re.match(r'^(\d+)\.(\d+)\.(\d+)\.(\d+)$', ip, re.IGNORECASE):
        return False


    parts = ip.split('.')

    for part in parts:
        try:
            num = int(part)
        except ValueError:
            return False
        
        if part.startswith('0') and len(part) > 1:
            return False

        if not (num >= 0 and num <= 255):
            return False
        
    return True




if __name__ == "__main__":
    main()