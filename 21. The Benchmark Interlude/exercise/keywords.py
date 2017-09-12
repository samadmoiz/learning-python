#!/usr/bin/env python3

from operator import add
from functools import reduce


def adder(good=3, bad=2, ugly=1):
    print('adder', end=' ')
    return good + bad + ugly

# print(adder())
# print(adder(1))
# print(adder(1, 2))
# print(adder(1, 2, 3))
# print(adder(ugly=10, bad=-2))


def adder1(**kwargs):
    print('adder1', end=' ')
    sum = 0
    for values in kwargs.values():
        sum += values
    return sum


def adder2(**kwargs):
    print('adder2', end=' ')
    args = list(kwargs.values())  # list need in 3.x
    tot = args[0]
    for arg in args:
        tot += arg
    return tot


def adder3(*args):
    return reduce(add, args)


def adder4(**kwargs):
    print('adder4', end=' ')
    args = list(kwargs.values())
    return adder3(*args)


for func in (adder, adder1, adder2, adder4):
    print(func(good=300, bad=200, ugly=100))
    if func is not adder:
        print(func(good=300, bad=200, ugly=100))
        print(func(awesome=10000, ugly=-1000))
