#!/usr/bin/env python3


def func(a, b, c):
    return a + b + c


# annotes
def func(a: 'spam', b: (1, 10), c: float) -> int:
    return a + b + c

print(func(1, 2, 3))

def func(a: 'spam' = 4, b: (1, 10) = 5, c: float = 6) -> int:
    return a + b + c

print(func(b=10))
