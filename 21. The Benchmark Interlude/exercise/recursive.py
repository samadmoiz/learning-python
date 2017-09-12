#!/usr/bin/env python3


# recursive
def countdown(n):
    if n == 0:
        print('stop')
    else:
        print(n, end=' ')
        countdown(n - 1)


n = 5
list(range(n, 0, -1))


t = [print(i, end=' ') for i in range(n, 0, -1)]


t = list(map(lambda x: print(x, end=' '), range(n, 0, -1)))


def countdown1(n):
    if n == 0:
        yield 'stop'
    else:
        yield n
        for x in countdown(n - 1):
            yield x


def countdown2(n):
    return (n for n in range(n, 0, -1))


def countdown3(n):
    for n in range(n, 0, -1):
        yield n


def countdown4(n):
    yield from range(n, 0, -1)

print(countdown1(5))
