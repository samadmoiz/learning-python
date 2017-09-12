#!/usr/bin/env python3


def copydict(d):
    print('copydict', end=' ')
    keys = list(d.keys())
    new = {}
    for key in keys:
        new[key] = d[key]
    return new


D = {'a': 1, 'b': 2, 'c': 3}
print(copydict(D))


def add_dict(d1, d2):
    print('add_dict', end=' ')
    new = {}
    for key in d1.keys():
        new[key] = d1[key]
    for key in d2.keys():
        new[key] = d2[key]
    return new

print(add_dict(D, {'a': 2, 'd': 4}))
