string = input('Enter your word: ')

count = 0
for i in range(0, len(string)):
    if string[i] != 'e' and (count-1) % 2 == 0:
        print(string[count])
    count += 1
