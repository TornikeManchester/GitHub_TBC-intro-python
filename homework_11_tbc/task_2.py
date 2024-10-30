a = int(input('Enter your number: '))
b = int(input('Enter your number: '))

if a > 10000 or b > 10000 and a < 0 or b < 0:
    print('Please enter numbers between 0 and 10000')
    exit(1)

def gcd_iter(a, b):
    m = min(a, b)
    while m > 0:
        if a % m == 0 and b % m == 0:
            return m
        m -= 1

    return m

def gcd_recur(a, b):
    if b == 0:
        return a
    else:
        return gcd_recur(b, a % b)

def main():
    print(f"GCD of {a} and {b} is {gcd_iter(a, b)}")
    print(f"GCD of {a} and {b} is {gcd_recur(a, b)}")

if __name__ == "__main__":
    main()
