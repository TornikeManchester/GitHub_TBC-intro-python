import random

number = int(input('Enter number: '))

if number > 30:
    exit(1)
elif number <= 0:
    exit(1)
else:
    for i in range(number):
        print(random.randint(1,1001))