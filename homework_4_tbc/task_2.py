import random

number = int(input('Enter number: '))

if 0 < number < 30:
    max_value = max(random.randint(1, 1001)
        for i in range(number))
    print("Maximum value:", max_value)
else:
    print("უნდა შეიყვანოთ რიცხვი 0-დან 30-მდე დიაპაზონში")
    exit(1)
