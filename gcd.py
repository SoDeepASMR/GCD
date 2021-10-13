import sys

a, b = int(sys.argv[1]), int(sys.argv[2])

def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print('НОД =', a)

gcd(a, b)
