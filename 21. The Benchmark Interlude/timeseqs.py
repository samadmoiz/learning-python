# File timeseqs.py
"Test the relative speed of iteration tool alternatives."

import sys
import timer

reps = 10000
repslist = list(range(reps))  # Hoist out, list in both 2.X/3.X


def forloop():
    res = []
    for i in repslist:
        res.append(abs(i))
    return res


def listComp():
    return [abs(x) for x in repslist]


def mapCall():
    return list(map(abs, repslist))  # use list() here in 3.x only
    # return map(abs, repslist)


def genExp():
    return list(abs(x) for x in repslist)  # list required to force the result


def genFunc():
    def gen():
        for i in repslist:
            yield abs(i)
    return list(gen())  # list required to force the result

print(sys.version)
for test in (forloop, listComp, mapCall, genExp, genFunc):
    (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
    print('%-9s: %.5f => [%s...%s]' %
          (test.__name__, bestof, result[0], result[-1]))
