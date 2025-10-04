import argparse

# python 08_real_argparse.py -n 3
# python 08_real_argparse.py -h

parser = argparse.ArgumentParser(description="meow like a cat")
parser.add_argument("-n", help="number of times to print meow")
args = parser.parse_args()

print(args.n)
