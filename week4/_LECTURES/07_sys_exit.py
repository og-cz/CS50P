import sys

#  python 07_sys_exit.py ogcz qdasd


if len(sys.argv) < 2:
    sys.exit("too few arguments")

for arg in sys.argv:
    print("hello my name is", arg)

# outputs:
# hello my name is 07_sys_exit.py
# hello my name is ogcz
# hello my name is qdasd
