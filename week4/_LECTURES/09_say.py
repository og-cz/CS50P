import cowsay  # type: ignore
import sys


if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])

# outputs
# python 09_say.py david
#   ____________
# | hello, david |
#   ============
#             \
#              \
#                ^__^
#                (oo)\_______
#                (__)\       )\/\
#                    ||----w |
#                    ||     ||


if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])
