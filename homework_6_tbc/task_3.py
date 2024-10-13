number = (input('Enter your number: '))

if int(number) < 0 or int(number) > 10000:
    print('Enter your number between 0 and 10000')
    exit(1)
else:
    count = 0
    digits_sum = 0
    while count < len(number):
        #print(number[count])
        digits_sum += int(number[count])
        count += 1

print(f'enter number: {number}')
print(f'reversed number is {number[::-1]}')
print(f'sum of digits is {digits_sum}')

