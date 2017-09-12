def intersect(*args):
    res = []
    for x in args[0]:
        if x in res:
            continue
        for other in args[1:]:
            if x not in other:
                break
        else:
            res.append(x)
    return res

s1, s2 = "spam", "scam"
print(intersect(s1, s2))


def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if x not in res:
                res.append(x)
    return res

print(union(s1, s2))
