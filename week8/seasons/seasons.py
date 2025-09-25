from datetime import date
import sys
import inflect

p = inflect.engine()

class BirthDate:
    months = ('01','02','03','04','05','06','07','08','09','10','11','12')

    def __init__(self, birth_str: str):
        try:
            year, month, day = birth_str.split('-')
            self.birthdate = date(int(year), int(month), int(day))
        except Exception:
            sys.exit("Invalid date")

    def minutes_lived(self):
        today = date.today()
        delta = today - self.birthdate
        return delta.days * 24 * 60

def main():
    birthdate = get_date(input('Date of Birth: '))
    minutes_str = get_minutes_lived(birthdate)
    print(convert_into_words(minutes_str))

def get_date(birthdate):
    return BirthDate(birthdate)

def get_minutes_lived(birthdate):
    return birthdate.minutes_lived()

def convert_into_words(minutes: int) -> str:
    words = p.number_to_words(minutes, andword='')
    words = words[0].upper() + words[1:]
    return f"{words} minutes"

if __name__ == "__main__":
    main()

