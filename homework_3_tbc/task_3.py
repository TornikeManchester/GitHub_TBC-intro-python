import datetime

birth_year = input('Enter your birth year: ')
birth_month = input('Enter your birth month: ')
birth_day = input('Enter your birth day: ')

day_of_birth = datetime.date(int(birth_year), int(birth_month), int(birth_day))

print(day_of_birth.strftime('%A'))

