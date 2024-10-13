number = int(input('Enter your number: '))

if number > 1000 or number <0:
    print('Enter number between 0 and 1000')
    exit(1)
else:
    while number != 1:
        if number % 2 == 0:
            number = (number / 2)
        else:
            number = (number * 3 + 1)
        print(number)
