string = input('Enter your word: ')

count = 0
if len(string) % 2 != 0:
    while count < 5:
        if len(string) % 2 != 0:
            print(string[len(string)-1] + string[0] + string[(len(string) // 2)])
        count += 1
else:
    print(string[(round(len(string) / 2) - 1)] + string[(round(len(string) / 2))])
