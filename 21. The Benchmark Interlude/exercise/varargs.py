#!/usr/bin/env python3

from operator import add
from functools import reduce


def adder(*args):
    print('adder', end=' ')
    return reduce(add, args)


def adder1(*args):
    print('adder1', end=' ')
    if type(args[0]) == type(0):
        sum = 0
    else:
        sum = args[0][:0]
    for arg in args:
        sum = sum + arg
    return sum


def adder2(*args):
    # print('adder1', end=' ')
    sum = args[0]
    for arg in args[1:]:
        sum += arg
    return sum


for func in (adder, adder1, adder2):
    print(func(1, 2, 3, 4))
    print(func('spam', 'ham', 'eggs'))
    print(func(['a', 'b'], ['c', 'd'], ['e', 'f']))
