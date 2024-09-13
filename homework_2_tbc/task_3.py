intenger_number = input('select your intenger number: ')

if int(intenger_number) > 10 or int(intenger_number) < 1:
    exit(1)

if int(intenger_number) % 2 == 0:
    if int(intenger_number) % 3 == 0:
        print('2 and 3')
    elif int(intenger_number) % 4 == 0:
        print('2 and 4')
    elif int(intenger_number) % 5 == 0:
        print('2 and 5')
    else:
        print('2')
elif int(intenger_number) % 3 == 0:
    if int(intenger_number) % 9 == 0:
        print('3')
    else:
        print('3')
elif int(intenger_number) % 5 == 0:
    print('5')
elif int(intenger_number) % 7 == 0:
    print('7')
else:
    print('1')