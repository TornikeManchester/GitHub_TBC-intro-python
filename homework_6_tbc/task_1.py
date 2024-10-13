import random

counter = 1
while counter < 10:
    random_number = random.randint(0, 100)
    human_number = int(input('Enter your number: '))
    print(f'random_number: {random_number}, human_number: {human_number}')
    if human_number > random_number:
        print('high')
    elif human_number < random_number:
        print('low')
    else:
        print('You are winner')
    counter += 1
else:
    print('Computer is winner')
