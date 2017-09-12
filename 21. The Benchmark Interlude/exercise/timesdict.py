import sys
import timer2

def dictcomp(I):
    return {i: i for i in range(I)}


def dictloop(I):
    new = {}
    for i in range(I):
        new[i] = i
    return new


print(sys.version)
for test in (dictcomp, dictloop):
    elapsed, result = timer2.bestof(test, 10000)
    # timer2.bestof(test, 100000)  # 100,000 items: 10x slower
    # timer2.bestof(test, 1000000)  # 1 to 1M-items: 10x time
    # timer2.total(test, 1000000, _reps=50)  # Total to make 50 1M-items dict
    print('%s: %.5f' % (test.__name__, elapsed))
