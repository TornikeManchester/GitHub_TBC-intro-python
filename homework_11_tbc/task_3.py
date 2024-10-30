from task_2 import gcd_iter

a = int(input('Enter your number: '))
b = int(input('Enter your number: '))

if a > 10000 or b > 10000 and a < 0 or b < 0:
    print('Please enter numbers between 0 and 10000')
    exit(1)

def lcm_iter(a, b):
    return a * b // gcd_iter(a, b)

def main():
    print(lcm_iter(a, b))

if __name__ == "__main__":
    main()
