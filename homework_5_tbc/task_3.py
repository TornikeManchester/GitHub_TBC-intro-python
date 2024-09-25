number = int(input('Enter your number: '))

if number > 0 and number < 20:
    if number == 0:
        result = 0
    elif number == 1:
        result = 1
    else:
        i = 1
        a = 0
        b = 1
        print(a, end=' ')
        print(b, end=' ')
        while i < number:
            c = a + b
            a = b
            b = c
            result = b
            i += 1
            print(result, end=' ')
else:
    print('Enter number between 0 and 20')
    exit(1)

