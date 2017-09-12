#!/usr/bin/env python3


def mysum(L, trace=False):
    if trace:
        print(L)
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:], trace)

print(mysum([1, 2, 3]))
print()
print(mysum([1, 2, 3], trace=True))


# Coding Alternative

def mysum(L):
    return 0 if not L else L[0] + mysum(L[1:])


def mysum(L):
    return L[0] if len(L) == 1 else L[0] + mysum(L[1:])


def mysum(L):
    first, *rest = L
    return first if not rest else first + mysum(rest)


# Indirectly recursion
def mysum(L):
    if not L:
        return 0
    else:
        return nonempty(L)


def nonempty(L):
    return L[0] + mysum(L[1:])


print(mysum([1.1, 2.2, 3.3, 4.4]))
