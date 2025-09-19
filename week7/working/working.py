import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError as e:
        sys.exit(e)

def convert(s):
        try:
            pattern = r'^(1[0-2]|0?[1-9]):?([0-5][0-9])? (AM|PM) to (1[0-2]|0?[1-9]):?([0-5][0-9])? (AM|PM)$'
            matches = re.search(pattern, s, re.IGNORECASE)
        except ValueError:
            sys.exit(1)

        if matches:
            start_hour, start_minute, start_period, end_hour, end_minute, end_period = matches.groups()

            start_minute = start_minute or "00"
            end_minute = end_minute or "00"

            if not(1 <= int(start_hour) <= 12):
               raise ValueError('ValueError')
            if not(1 <= int(end_hour) <= 12):
                raise ValueError('ValueError')
            if not(0 <= int(start_minute) <= 59):
                raise ValueError('ValueError')
            if not(0 <= int(end_minute) <= 59):
                raise ValueError('ValueError')

            if start_period.upper() == 'PM' and start_hour != '12':
                start_hour = str(int(start_hour) + 12)
            elif start_period.upper() == 'AM' and start_hour == '12':
                start_hour = '00'

            if end_period.upper() == 'PM' and end_hour != '12':
                end_hour = str(int(end_hour) + 12)
            elif end_period.upper() == 'AM' and end_hour == '12':
                end_hour = '00'

            start_hour = str(start_hour).zfill(2)
            end_hour = str(end_hour).zfill(2)
            start_minute = str(start_minute).zfill(2)
            end_minute = str(end_minute).zfill(2)

            return f'{start_hour}:{start_minute} to {end_hour}:{end_minute}'
        else:
            raise ValueError('ValueError')



if __name__ == "__main__":
    main()