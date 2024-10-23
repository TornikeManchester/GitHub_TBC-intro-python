n = int(input('Enter your number: '))

if n < 1:
    print('Enter your number more than 1')
    exit(1)
else:
    series_sum = 0

    for i in range(n):
        term = (-1) ** i / (2 * i + 1)
        series_sum += term

    pi_approx = 4 * series_sum
    print(pi_approx)