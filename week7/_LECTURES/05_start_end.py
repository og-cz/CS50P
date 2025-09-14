import re

email = input("enter a email ").rstrip()

# my email adress is malan@harvard.edu. -> invalid

if re.search(r"^.+@.+\.edu$",email): 
    print('valid')
else:
    print("invalid")