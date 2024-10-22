import re

text = input('Enter your text: ')
text = text.lower()
clean_string = re.sub(r'[^A-Za-z0-9]', '', text)

if clean_string[:] == clean_string[::-1]:
    print('It is palindrome')
else:
    print('It is not palindrome')
