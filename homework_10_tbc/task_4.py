def is_prime(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count > 2:
        print('it is not prime number')
    else:
        print('it is prime number')
