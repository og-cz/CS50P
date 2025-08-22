import sys

import a11_custom_libraries

# python a12_custom_test.py david


if len(sys.argv) == 2:
    a11_custom_libraries.hello(sys.argv[1])

a11_custom_libraries.main()
