import re

email = input("enter a email ").rstrip()

# \w+ = word character with 1 or more 
# @ = literal @
# (edu|edu|com|net) = either one of them

if re.search(r"^\w+@\w+\.(edu|edu|com|net)$",email): 
    print('valid')
else:
    print("invalid")