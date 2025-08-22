import sys

#  python 06_sys_argv.py ogcz

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Index Error, too few arguments.")
print(sys.argv[0])


if len(sys.argv) < 2:
    print("too few arguments.")
elif len(sys.argv) > 2:
    print("too many arguments.")
else:
    print("hello, my name is", sys.argv[1])
