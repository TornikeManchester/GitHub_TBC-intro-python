number = int(input('Enter your number: '))

if number < 0 or number > 10:
    print('Enter your number between 0 and 10')
    exit(1)
else:
    i = 1
    while i <= number:
        j = 1
        while j <= i:
            print(j,end=" ")
            j += 1
        print()
        i += 1

    i = number - 1
    while i > 0:
        j = 1
        while j <= i:
            print(j,end=" ")
            j += 1
        print()
        i -= 1