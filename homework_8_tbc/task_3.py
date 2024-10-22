time = input('Select your timezone: ')

timetable = time[11:19]
hours, minutes, seconds = timetable.split(':')
hours = int(hours)

if hours > 12:
    hours -= 12
elif hours == 12:
    hours == 12

print(f'{time[8:10]}-{time[5:7]}-{time[:4]} '
      f'{hours}{time[13:19]} {time[-6]}{time[-4]}')