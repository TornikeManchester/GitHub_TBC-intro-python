car_speed = input('car speed is: ')

if int(car_speed) < 30:
    print('slow')
elif int(car_speed) > 120:
    print('very fast')
elif int(car_speed) > 60 and int(car_speed) <= 120:
    print('fast')
else:
    print('moderate')