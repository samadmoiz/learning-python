def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res


def min2(first, *rest):
    for arg in rest:
        if arg < first:
            first = arg
    return first


def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]


print(min1(1, 2, 0, 2, 3))

print(min2("bb", "aa", "bb", "cc"))

print(min3([1, 2], [1, 3], [3, 3]))
