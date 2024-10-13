number = int(input('Enter your number: '))

if number < 0 or number > 10:
    print('Enter your number between 0 and 10')
    exit(1)
else:
    i = 0
    while i <= number:
        spaces = number - i
        while spaces > 0:
            print(' ',end=' ')
            spaces -= 1

        j = i
        while j > 0:
            print(j,end=' ')
            j -= 1

        j = 0
        while j <= i:
            print(j,end=' ')
            j += 1
        i += 1
        print()