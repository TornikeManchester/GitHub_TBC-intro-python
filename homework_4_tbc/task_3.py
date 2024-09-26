number = int(input('Enter number: '))

if number > 1000:
    exit(1)
elif number <= 0:
    exit(1)
else:
    for i in range(1, number + 1):
        if number % i == 0:
            print(i, end=' ')

