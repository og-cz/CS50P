import sys

#  python 08_slices.py wa we wi wo wu


if len(sys.argv) < 2:
    sys.exit("too few arguments")

for arg in sys.argv[1:]:
    print("hello my name is", arg)

# outputs:
# hello my name is wa
# hello my name is we
# hello my name is wi
# hello my name is wo
# hello my name is wu
