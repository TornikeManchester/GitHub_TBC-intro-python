number = int(input('Enter number: '))

if number > 20 or number <= 0:
    exit(1)
if number == 0:
    result = 0
elif number == 1:
    result = 1
else:
    a, b = 0, 1
    for i in range(2, number + 1):
        c = a + b
        a = b
        b = c
    result = b
print(result)
