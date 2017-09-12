from math import sqrt


L = [2, 4, 9, 16, 25]

L1 = []
for x in L:
    L1 += [sqrt(x)]  # L1.append(sqrt(x))

print(L1)


L2 = [sqrt(x) for x in L]


L3 = map(sqrt, L)


L4 = (sqrt(x) for x in L)


def g():
    for x in L:
        yield sqrt(x)
L5 = g()


for l in (L1, L2, L3, L4, L5):
    print(list(l))
