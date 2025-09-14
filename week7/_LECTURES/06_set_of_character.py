import re

email = input("enter a email ").rstrip()

# my email adress is malan@@@harvard.edu -> invalid

# [^@] this is any set of characters except @ sign
#[a-zA-Z] this means any set of characters a to z and A TO Z

if re.search(r"^[a-zA-Z0-9_ ]+@[^@]+\.edu$",email): 
    print('valid')
else:
    print("invalid")