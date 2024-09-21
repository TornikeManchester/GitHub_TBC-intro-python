import random

player_number = int(input('Enter player number: '))

for i in range(player_number):
    random_1 = random.randint(1, 6)
    random_2 = random.randint(1, 6)
    if random_1 == random_2:
        if random_2 == 6:
            random_2 = 1
        else:
            random_2 += 1

    print(random_1, random_2)