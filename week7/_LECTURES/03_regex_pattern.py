import re

email = input("enter a email ").rstrip()

# this check ( .* ) and ( @ ) and ( .* )  meaning -> abc@abc, a@a, @ are all valid

# if re.search(".*@.*",email): 
#     print('valid')
# else:
#     print("invalid")

if re.search(".+@.+",email): 
    print('valid')
else:
    print("invalid")