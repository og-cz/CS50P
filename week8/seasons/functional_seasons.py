# from datetime import date
# import sys

# class Date:
#     months = ('01','02','03','04','05','06','07','08','09','10','11','12')

# def main():
#     birthdate = get_date(input('Date of Birth: '))
#     print(minutes_lived(birthdate))
    
# def get_date(birth):
#     year, month, day = (int(x) for x in validate(birth))
#     birthdate = date(year,month,day)
#     return birthdate

# def minutes_lived(birthdate):
#     today = date.today()
#     delta = today - birthdate
#     return delta.days * 24 *60

# def validate(birth):
#     try:
#         year, month, day = birth.split('-', -1)

#         # months validation
#         if month not in Date.months:
#             raise ValueError('Invalid date')
        
#         # day validation
#         if not 1 <= int(day) <= 31:
#             raise ValueError('Invalid date')

#         return year, month, day
#     except (ValueError) as e:
#         print('Invalid date')
#         sys.exit(1)

# if __name__ == "__main__":
#     main()
