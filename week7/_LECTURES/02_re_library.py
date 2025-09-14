import re
email = input("enter email ").strip()
# malan@harvard.edu

# this is no better to 01_validate just using the library
if re.search('@', email):
    print('valid')
else:
    print('invalid')