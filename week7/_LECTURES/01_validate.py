email = input("enter email ").strip()

if '@' in email and '.' in email: # two boolean expression
    print('valid')
else:
    print("invalid")

print(email)
print("===================================================================")

# this just splits the email part for more checking
name, domain = email.split("@")

if name and '.' in domain: # checking if empty and checking . in the domain
    print("valid")
else: 
    print('invalid')

print('username :', name)
print('domain :', domain)