import time

a = int(input('Enter your number: '))
b = int(input('Enter your number: '))

if (a > 10000 or b > 10000) or (a < 0 or b < 0):
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
    start_time = time.time()  # start
    gcd_result_iter = gcd_iter(a, b)
    end_time = time.time()  # end
    print("Iterative GCD result:", gcd_result_iter)
    print("Time passed (iterative):", end_time - start_time)

    start_time = time.time()  # start
    gcd_result_recur = gcd_recur(a, b)
    end_time = time.time()  # end
    print("Recursive GCD result:", gcd_result_recur)
    print("Time passed (recursive):", end_time - start_time)

if __name__ == "__main__":
    main()