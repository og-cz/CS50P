import sys
from validator_collection import validators

def main():
    validate_email(input('What\'s your email address? '))

def validate_email(email):
        try: 
            matches = validators.email(email)
            if matches:
                print('Valid')
        except (ValueError, TypeError, IOError) as e:
            print('Invalid')
            sys.exit(0)

if __name__ == '__main__':
    main()