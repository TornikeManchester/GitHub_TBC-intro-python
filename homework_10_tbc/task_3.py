def factorial(number):
    count = 1
    for i in range(1, int(number) + 1):
        count *= i
    print(count)
