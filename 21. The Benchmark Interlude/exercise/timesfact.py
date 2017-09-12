import sys
import timeit
import math
from functools import reduce


def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)


def fact1(n):
    def f(a, b):
        return a * b
    return reduce(f, range(n, 0, -1))


def fact2(n):
    result = n
    for i in range(n-1, 0, -1):
        result *= i
    return result


def fact3(n):
    return math.factorial(n)


print(sys.version)
for test in (fact, fact1, fact2, fact3):
    def t():
        test(int(sys.argv[1]) if len(sys.argv) > 1 else 6)
    elapsed = min(timeit.repeat(number=1000, repeat=5, stmt=t))
    print('%s: %f' % (test.__name__, elapsed))
