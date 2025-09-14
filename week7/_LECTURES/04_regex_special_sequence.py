import re

email = input("enter a email ").rstrip()

# malan@harvard? -> invalid
# malan@harvard.com -> invalid

if re.search(r".+@.+\.edu",email): 
    print('valid')
else:
    print("invalid")