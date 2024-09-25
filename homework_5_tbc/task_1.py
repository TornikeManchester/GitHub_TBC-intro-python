number = int(input('Enter your number: '))

if number > 0 or number < 50:
    for i in range(1, number + 1):
        count = 0
        print(f"{i}-", end=' ')
        for j in range(1, i + 1):
            if i % j == 0:
                print(j, end=' ')
                count = count + 1
                if count == 3:
                    break
        print()
else:
    print('Select your number between 0 and 50')
    exit(1)