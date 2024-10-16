string = input('Enter your word: ')

for i in range(0, len(string)):
    if string[i] != 'a' and string[i] != 'e' and string[i] != 'o' and string[i] != 'u' and string[i] != 'i':
        print(string[i])