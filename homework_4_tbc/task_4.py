number = int(input('Enter number: '))

if number > 20:
    exit(1)
elif number <= 0:
    exit(1)
else:
    s = 0
    for i in range(number - 1):
        s += i
    print(s)